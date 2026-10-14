import time

from .logger import logger


def registrar_execucao(resultado, inicio):
    tempo_total = time.time() - inicio

    logger.info(
        f"Execução da Crew finalizada | "
        f"tempo total: {tempo_total:.2f}s"
    )

    for i, task_output in enumerate(
        resultado.tasks_output,
        start=1
    ):
        logger.info(
            f"Task {i} finalizada | "
            f"tamanho: {len(task_output.raw)} caracteres"
        )