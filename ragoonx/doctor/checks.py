from pathlib import Path

import app.settings as settings

from ragoonx.config import ConfigLoader


class DoctorChecks:

    @staticmethod
    def config_exists():

        try:

            ConfigLoader.load()

            return True

        except Exception:

            return False

    @staticmethod
    def groq_key():

        return bool(
            settings.GROQ_API_KEY
        )

    @staticmethod
    def qdrant_exists():

        return Path(
            settings.QDRANT_PATH
        ).exists()

    @staticmethod
    def bm25_exists():

        return Path(
            settings.BM25_INDEX_PATH
        ).exists()

    @staticmethod
    def documents_exist():

        return Path(
            settings.DOCUMENT_STORE_PATH
        ).exists()