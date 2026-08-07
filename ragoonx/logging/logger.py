import logging


class Logger:

    @staticmethod
    def create():

        logger = logging.getLogger("ragoonx")

        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(levelname)s] %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger


logger = Logger.create()