import re
import unicodedata
from urllib.parse import urlparse

from crewai.tools import BaseTool
from crewai_tools import SerperDevTool
from crewai.tools import tool
from pydantic import BaseModel, Field

from ..rag.retriever import search

search_tool = SerperDevTool()

class BuscaImoveisInput(BaseModel):
    cidade: str = Field(
        ...,
        description="Cidade onde os imóveis serão pesquisados."
    )
    tipo: str = Field(
        default="apartamento",
        description="Tipo de imóvel desejado."
    )
    preco_maximo: float | None = Field(
        default=None,
        gt=0,
        description="Preço máximo de venda em reais."
    )
    quartos: int | None = Field(
        default=None,
        ge=1,
        description="Quantidade mínima de quartos desejada."
    )
    area_minima: float | None = Field(
        default=None,
        gt=0,
        description="Área útil mínima em metros quadrados."
    )
    bairros: str | None = Field(
        default=None,
        description="Bairros desejados, separados por vírgulas."
    )


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    return "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    ).lower().strip()


def formatar_reais(valor: float) -> str:
    texto = f"{valor:,.2f}"
    texto = (
        texto.replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
    return f"R$ {texto}"


def url_valida(url: str) -> bool:
    try:
        partes = urlparse(url)
        return (
            partes.scheme in ("http", "https")
            and bool(partes.netloc)
        )
    except (ValueError, AttributeError):
        return False


def pesquisar(serper, consulta: str) -> list[dict]:
    """Executa uma consulta e retorna resultados orgânicos."""
    resposta = serper.run(search_query=consulta)

    if not isinstance(resposta, dict):
        return []

    resultados = resposta.get("organic", [])
    return resultados if isinstance(resultados, list) else []

def pesquisar_preco_anuncio(
    serper,
    titulo: str,
    url: str,
    cidade: str,
    tipo: str,
    preco_maximo: float | None = None,
) -> list[dict]:
    """Busca novamente um anúncio específico para tentar localizar o preço."""

    dominio = urlparse(url).netloc.removeprefix("www.")

    consulta = (
        f'site:{dominio} "{titulo}" "{cidade}" '
        f'"{tipo}" "à venda" preço'
    )

    if preco_maximo is not None:
        consulta += f' "R$ {int(preco_maximo)}"'

    try:
        return pesquisar(serper, consulta)
    except Exception:
        return []

def eh_agregadora(
    titulo: str,
    descricao: str,
    url: str,
) -> bool:
    """Identifica páginas de busca ou listagem de imóveis."""

    texto = normalizar(f"{titulo} {descricao}")
    partes_url = urlparse(url)
    caminho = normalizar(partes_url.path)
    parametros = normalizar(partes_url.query)

    termos_agregadores = [
        "apartamentos a venda",
        "apartamentos a venda ate",
        "imoveis a venda",
        "imoveis para venda",
        "resultados da busca",
        "resultado da pesquisa",
        "pagina de resultados",
        "encontre seu imovel",
        "imoveis encontrados",
        "apartamentos encontrados",
        "todos os imoveis",
    ]

    if any(termo in texto for termo in termos_agregadores):
        return True

    caminhos_agregadores = [
        "/busca",
        "/buscar",
        "/pesquisa-de-imoveis",
        "/imoveis-seo",
        "/venda/sp/",
        "/comprar/imovel/",
    ]

    if any(termo in caminho for termo in caminhos_agregadores):
        return True

    parametros_agregadores = [
        "valormax",
        "valormin",
        "dormmin",
        "dormmax",
        "areamin",
        "areamax",
        "search_type",
        "finalidade=",
        "categoria=",
        "cidade=",
    ]

    if any(termo in parametros for termo in parametros_agregadores):
        return True

    if re.search(
        r"\b\d{1,5}\s+(apartamentos|imoveis)\b",
        texto,
    ):
        return True

    return False


def extrair_precos(texto: str) -> list[float]:
    """
    Extrai valores monetários explícitos do texto.
    Remove URLs para não interpretar filtros como preços.
    """

    texto_sem_urls = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        texto,
        flags=re.IGNORECASE,
    )

    padrao = re.compile(
        r"R\$\s*"
        r"("
        r"\d{1,3}(?:\.\d{3})+(?:,\d{1,2})?"
        r"|\d{1,3}(?:,\d{3})+(?:\.\d{1,2})?"
        r"|\d+(?:[.,]\d{1,2})?"
        r")"
        r"\s*(milhões?|milhoes|milhão|milhao|mil)?",
        re.IGNORECASE,
    )

    valores = []

    for match in padrao.finditer(texto_sem_urls):
        numero = match.group(1)
        sufixo = normalizar(match.group(2) or "")

        if "," in numero and "." in numero:
            if numero.rfind(",") > numero.rfind("."):
                numero = numero.replace(".", "").replace(",", ".")
            else:
                numero = numero.replace(",", "")

        elif "," in numero:
            partes = numero.split(",")

            if len(partes[-1]) == 2:
                numero = (
                    "".join(partes[:-1]) + "." + partes[-1]
                )
            else:
                numero = "".join(partes)

        elif "." in numero:
            partes = numero.split(".")

            if len(partes[-1]) == 3:
                numero = numero.replace(".", "")
            elif len(partes[-1]) == 2:
                numero = (
                    "".join(partes[:-1]) + "." + partes[-1]
                )

        try:
            valor = float(numero)

            if sufixo.startswith("milh"):
                valor *= 1_000_000
            elif sufixo == "mil":
                valor *= 1_000

            if valor > 0:
                valores.append(valor)

        except ValueError:
            continue

    return valores


def extrair_preco_individual(
    titulo: str,
    descricao: str,
    agregadora: bool,
) -> float | None:
    """
    Extrai um preço somente quando o resultado não é agregador
    e o texto não contém sinais evidentes de ambiguidade.
    """

    if agregadora:
        return None

    texto = f"{titulo}. {descricao}"
    texto_n = normalizar(texto)

    termos_ambiguos = [
        "preco medio",
        "valor medio",
        "media de precos",
        "condominio",
        "aluguel",
        "locacao",
        "por mes",
        "mensal",
        "iptu",
        "a partir de",
        "sob consulta",
    ]

    if any(termo in texto_n for termo in termos_ambiguos):
        return None

    # Não confundir limites de preço com preço de venda.
    if re.search(
        r"\b(ate|entre)\s+R\$\s*"
        r"[\d.,]+\s*(?:milhoes?|milhoes|milhao|milhao|mil)?\b",
        texto,
        flags=re.IGNORECASE,
    ):
        return None

    valores = list(dict.fromkeys(extrair_precos(texto)))

    if len(valores) != 1:
        return None

    return valores[0]

def confirmar_preco_anuncio(
    serper,
    titulo: str,
    descricao: str,
    url: str,
    cidade: str,
    tipo: str,
    preco_maximo: float | None = None,
) -> float | None:
    """Confirma o preço usando uma pesquisa direcionada ao anúncio."""

    resultados = pesquisar_preco_anuncio(
        serper=serper,
        titulo=titulo,
        url=url,
        cidade=cidade,
        tipo=tipo,
        preco_maximo=preco_maximo,
    )

    url_original = url.rstrip("/").split("?")[0]

    for resultado in resultados:
        link_resultado = str(
            resultado.get("link", "")
        ).strip().rstrip("/").split("?")[0]

        if link_resultado != url_original:
            continue

        titulo_resultado = str(
            resultado.get("title", "")
        ).strip()

        descricao_resultado = str(
            resultado.get("snippet", "")
        ).strip()

        texto = f"{titulo_resultado}. {descricao_resultado}"
        texto_n = normalizar(texto)

        # A pesquisa precisa identificar explicitamente
        # o valor como preço ou valor do imóvel.
        padrao = (
            r"(?:valor do im[oó]vel|pre[cç]o de venda|"
            r"valor de venda|im[oó]vel por|"
            r"apartamento por|casa por)"
            r"\s*:?\s*R\$\s*"
            r"(\d{1,3}(?:\.\d{3})+(?:,\d{1,2})?"
            r"|\d+(?:,\d{1,2})?)"
        )

        match = re.search(
            padrao,
            texto,
            flags=re.IGNORECASE,
        )

        if not match:
            continue

        valores = extrair_precos(match.group(0))

        if len(valores) != 1:
            continue

        preco = valores[0]

        if preco_maximo is not None and preco > preco_maximo:
            continue

        return preco

    return None

def cidade_compativel(
    cidade: str,
    titulo: str,
    descricao: str,
    url: str,
) -> tuple[bool, str]:
    """Verifica se há evidência da cidade solicitada."""

    cidade_n = normalizar(cidade)
    texto = normalizar(f"{titulo} {descricao}")
    url_n = normalizar(url)

    cidade_no_texto = bool(
        re.search(rf"\b{re.escape(cidade_n)}\b", texto)
    )

    cidade_slug = cidade_n.replace(" ", "-")
    cidade_na_url = cidade_slug in url_n

    if not cidade_no_texto and not cidade_na_url:
        return False, "cidade solicitada não identificada no resultado"

    outras_cidades = [
        "hortolandia",
        "campinas",
        "guarulhos",
        "osasco",
        "santo andre",
        "sao bernardo do campo",
        "sao caetano do sul",
        "ferraz de vasconcelos",
        "jundiai",
        "belo horizonte",
        "barueri",
        "tramandai",
    ]

    for outra in outras_cidades:
        padrao = rf"\b(?:em|de|no|na)\s+{re.escape(outra)}\b"

        if re.search(padrao, texto) and outra not in cidade_n:
            return False, f"possível localização divergente: {outra}"

    return True, "cidade identificada no texto ou na URL"


def extrair_quartos(texto: str) -> list[int]:
    """Extrai quantidades de quartos ou dormitórios mencionadas."""

    texto_n = normalizar(texto)

    encontrados = re.findall(
        r"\b(\d+)\s*(?:quartos?|dormitorios?)\b",
        texto_n,
    )

    return [int(valor) for valor in encontrados]


def extrair_areas(texto: str) -> list[float]:
    """Extrai áreas explicitamente acompanhadas de m² ou m2."""

    texto_n = normalizar(texto)

    encontrados = re.findall(
        r"\b(\d+(?:[.,]\d+)?)\s*(?:m²|m2|metros quadrados)\b",
        texto_n,
    )

    areas = []

    for valor in encontrados:
        try:
            areas.append(float(valor.replace(",", ".")))
        except ValueError:
            continue

    return areas


def validar_bairro(
    bairros: str | None,
    texto: str,
) -> bool:
    """Verifica se pelo menos um bairro desejado aparece no texto."""

    if not bairros or not bairros.strip():
        return True

    texto_n = normalizar(texto)

    bairros_desejados = [
        normalizar(bairro)
        for bairro in bairros.split(",")
        if bairro.strip()
    ]

    return any(
        re.search(rf"\b{re.escape(bairro)}\b", texto_n)
        for bairro in bairros_desejados
    )


class BuscaImoveisTool(BaseTool):
    name: str = "buscar_imoveis"

    description: str = (
        "Pesquisa imóveis à venda com filtros de cidade, tipo, preço, "
        "quartos, área mínima e bairros. Separa candidatos preliminares "
        "de resultados que precisam de verificação."
    )

    args_schema: type[BaseModel] = BuscaImoveisInput

    def _run(
        self,
        cidade: str,
        tipo: str = "apartamento",
        preco_maximo: float | None = None,
        quartos: int | None = None,
        area_minima: float | None = None,
        bairros: str | None = None,
    ) -> str:

        cidade = cidade.strip()
        tipo = tipo.strip()
        bairros = (bairros or "").strip()

        if not cidade:
            return "Erro: informe a cidade da pesquisa."

        if not tipo:
            return "Erro: informe o tipo de imóvel."

        if preco_maximo is not None and preco_maximo <= 0:
            return "Erro: o preço máximo deve ser maior que zero."

        if quartos is not None and quartos < 1:
            return "Erro: a quantidade de quartos deve ser positiva."

        if area_minima is not None and area_minima <= 0:
            return "Erro: a área mínima deve ser maior que zero."

        consulta_geral = (
            f'"{tipo}" "à venda" "{cidade}" '
            f'("quartos" OR "dormitórios")'
        )

        consulta_portais = (
            f'"{tipo}" "à venda" "{cidade}" '
            f'("m²" OR "metros quadrados") '
            f'(site:imovelweb.com.br OR site:chavesnamao.com.br '
            f'OR site:vivareal.com.br OR site:quintoandar.com.br)'
        )

        if preco_maximo is not None:
            filtro_preco = f' até R$ {int(preco_maximo)}'
            consulta_geral += filtro_preco
            consulta_portais += filtro_preco

        if quartos is not None:
            filtro_quartos = f' "{quartos} quartos"'
            consulta_geral += filtro_quartos
            consulta_portais += filtro_quartos

        if area_minima is not None:
            filtro_area = f' "{int(area_minima)} m²"'
            consulta_geral += filtro_area
            consulta_portais += filtro_area

        if bairros:
            lista_bairros = [
                bairro.strip()
                for bairro in bairros.split(",")
                if bairro.strip()
            ]

            if lista_bairros:
                filtro_bairros = " (" + " OR ".join(
                    f'"{bairro}"' for bairro in lista_bairros
                ) + ")"

                consulta_geral += filtro_bairros
                consulta_portais += filtro_bairros

        try:
            serper = SerperDevTool()

            resultados_gerais = pesquisar(serper, consulta_geral)
            resultados_portais = pesquisar(serper, consulta_portais)

        except Exception as erro:
            return f"Erro ao pesquisar imóveis no Serper: {erro}"

        # Combina resultados e remove URLs duplicadas.
        resultados_unicos = {}

        for item in resultados_gerais + resultados_portais:
            if not isinstance(item, dict):
                continue

            link = str(item.get("link", "")).strip()

            if not url_valida(link):
                continue

            if link not in resultados_unicos:
                resultados_unicos[link] = item

        compativeis = []
        verificar = []
        descartados = []

        for link, item in resultados_unicos.items():
            titulo = str(item.get("title", "")).strip()
            descricao = str(item.get("snippet", "")).strip()

            if not titulo:
                continue

            texto_n = normalizar(f"{titulo} {descricao}")

            # Descarta resultados claramente identificados como aluguel.
            if any(
                termo in texto_n
                for termo in (
                    "para alugar",
                    "aluguel mensal",
                    "locacao de apartamento",
                    "apartamento para locacao",
                )
            ):
                descartados.append({
                    "titulo": titulo,
                    "link": link,
                    "motivo": "resultado identificado como aluguel",
                })
                continue

            agregadora = eh_agregadora(titulo, descricao, link)

            cidade_ok, motivo_cidade = cidade_compativel(
                cidade,
                titulo,
                descricao,
                link,
            )

            preco = extrair_preco_individual(
                titulo,
                descricao,
                agregadora,
            )

            if preco is None and not agregadora:
                preco = confirmar_preco_anuncio(
                    serper=serper,
                    titulo=titulo,
                    descricao=descricao,
                    url=link,
                    cidade=cidade,
                    tipo=tipo,
                    preco_maximo=preco_maximo
                )

            texto_imovel = normalizar(f"{titulo} {descricao}")

            # Os trechos indexados podem misturar dados de anúncios.
            # Só aprovamos quando há evidências mínimas de cada critério.
            quartos_ok = True

            if quartos is not None:
                quartos_encontrados = extrair_quartos(texto_imovel)

                quartos_ok = (
                    bool(quartos_encontrados)
                    and max(quartos_encontrados) >= quartos
                )

            area_ok = True

            if area_minima is not None:
                areas_encontradas = extrair_areas(texto_imovel)

                area_ok = (
                    bool(areas_encontradas)
                    and max(areas_encontradas) >= area_minima
                )

            bairro_ok = validar_bairro(bairros, texto_imovel)

            motivos = []

            if agregadora:
                motivos.append(
                    "página agregadora, não anúncio individual"
                )

            if not cidade_ok:
                motivos.append(motivo_cidade)

            if preco is None:
                motivos.append(
                    "preço individual não identificado com segurança"
                )
            elif preco_maximo is not None and preco > preco_maximo:
                motivos.append("preço acima do limite informado")

            if not quartos_ok:
                motivos.append(
                    "quantidade de quartos não confirmada ou insuficiente"
                )

            if not area_ok:
                motivos.append(
                    "área mínima não confirmada ou insuficiente"
                )

            if not bairro_ok:
                motivos.append("bairro desejado não identificado")

            registro = {
                "titulo": titulo,
                "link": link,
                "descricao": descricao,
                "preco": preco,
                "agregadora": agregadora,
                "motivos": motivos,
            }

            if (
                not agregadora
                and cidade_ok
                and preco is not None
                and (preco_maximo is None or preco <= preco_maximo)
                and quartos_ok
                and area_ok
                and bairro_ok
            ):
                compativeis.append(registro)
            else:
                verificar.append(registro)

        linhas = [
            f"Cidade solicitada: {cidade}",
            f"Tipo de imóvel: {tipo}",
            f"Consulta geral: {consulta_geral}",
            f"Consulta direcionada: {consulta_portais}",
        ]

        if preco_maximo is not None:
            linhas.append(
                f"Preço máximo: {formatar_reais(preco_maximo)}"
            )

        if quartos is not None:
            linhas.append(f"Quartos mínimos: {quartos}")

        if area_minima is not None:
            linhas.append(f"Área mínima: {area_minima:g} m²")

        if bairros:
            linhas.append(f"Bairros desejados: {bairros}")

        linhas.extend([
            "",
            "AVISO: os resultados vêm de trechos indexados. "
            "A classificação não confirma preço atual, disponibilidade "
            "ou características. Confirme os dados na página original.",
            "",
            f"Anúncios potencialmente compatíveis: {len(compativeis)}",
        ])

        for i, item in enumerate(compativeis, start=1):
            linhas.extend([
                "",
                f"{i}. {item['titulo']}",
                f"Descrição: {item['descricao'] or 'Não informada'}",
                f"Preço mencionado: {formatar_reais(item['preco'])}",
                f"Fonte: {item['link']}",
                "Status: compatibilidade preliminar; confirmar na fonte.",
            ])

        linhas.extend([
            "",
            f"Resultados que exigem verificação: {len(verificar)}",
        ])

        for i, item in enumerate(verificar, start=1):
            linhas.extend([
                "",
                f"Verificação {i}: {item['titulo']}",
                f"Descrição: {item['descricao'] or 'Não informada'}",
                (
                    f"Preço mencionado: {formatar_reais(item['preco'])}"
                    if item["preco"] is not None
                    else "Preço individual: não identificado com segurança"
                ),
                (
                    "Tipo de página: agregadora"
                    if item["agregadora"]
                    else "Tipo de página: possível anúncio individual"
                ),
                f"Fonte: {item['link']}",
                f"Motivo: {', '.join(item['motivos'])}.",
            ])

        linhas.extend([
            "",
            f"Resultados descartados: {len(descartados)}",
        ])

        for i, item in enumerate(descartados, start=1):
            linhas.extend([
                "",
                f"Descartado {i}: {item['titulo']}",
                f"Fonte: {item['link']}",
                f"Motivo: {item['motivo']}.",
            ])

        if not compativeis and not verificar:
            linhas.append(
                "\nNenhum resultado utilizável foi encontrado. "
                "Tente alterar os critérios."
            )

        return "\n".join(linhas)


imoveis_tool = BuscaImoveisTool()