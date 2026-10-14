from .logger import logger


def registrar_erro(etapa, erro):
    logger.error(
        f"Erro na etapa '{etapa}' | "
        f"tipo: {type(erro).__name__} | "
        f"mensagem: {erro}"
    )