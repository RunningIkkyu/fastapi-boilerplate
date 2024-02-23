import sys

from loguru import logger


def init_logger():
    logger.remove()
    format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    logger.configure(extra={"service_name": "sengine-workflow-api"})
    logger.add(
        sink="/tmp/app.log",
        level="INFO",
        rotation="100 MB",
        format=format,
        serialize=True,
    )
    logger.add(
        sys.stderr,
        format=format,
    )
