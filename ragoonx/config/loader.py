import os
import re
from pathlib import Path

import yaml

from ragoonx.config.defaults import DEFAULT_CONFIG

from ragoonx.config.models import (
    RagoonConfig,
    LLMConfig,
    EmbeddingConfig,
    RetrievalConfig,
    ChunkingConfig,
    StorageConfig,
    DataConfig,
)


class ConfigLoader:

    ENV_PATTERN = re.compile(r"\$\{(.*?)\}")

    CONFIG_FILE = "ragoonx.yaml"

    # --------------------------------------------------
    # Load Configuration
    # --------------------------------------------------

    @classmethod
    def load(cls, path=None):

        # -------------------------
        # User config
        # -------------------------

        if path is None:

            user_config = Path.cwd() / cls.CONFIG_FILE

            if user_config.exists():

                path = user_config

            else:

                # -------------------------
                # Packaged default config
                # -------------------------

                path = (
                    Path(__file__).resolve().parent
                    / "defaults.yaml"
                )

        else:

            path = Path(path)

        # -------------------------
        # Load YAML
        # -------------------------

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:

            config = yaml.safe_load(f) or {}

        # -------------------------
        # Environment variables
        # -------------------------

        config = cls._expand_env(config)

        # -------------------------
        # Merge defaults
        # -------------------------

        config = cls._merge_defaults(
            DEFAULT_CONFIG,
            config,
        )

        # -------------------------
        # Convert to model
        # -------------------------

        return cls._to_model(
            config
        )

    # --------------------------------------------------
    # Initialize User Configuration
    # --------------------------------------------------

    @classmethod
    def initialize(cls):

        path = Path.cwd() / cls.CONFIG_FILE

        # -------------------------
        # Don't overwrite existing
        # config
        # -------------------------

        if path.exists():

            print(
                f"{cls.CONFIG_FILE} already exists."
            )

            return

        # -------------------------
        # Create config from defaults
        # -------------------------

        config = DEFAULT_CONFIG.copy()

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:

            yaml.safe_dump(
                config,
                f,
                sort_keys=False,
            )

        print(
            f"Created {cls.CONFIG_FILE}"
        )

    # --------------------------------------------------
    # Environment Variable Expansion
    # --------------------------------------------------

    @classmethod
    def _expand_env(cls, obj):

        if isinstance(obj, dict):

            return {
                k: cls._expand_env(v)
                for k, v in obj.items()
            }

        if isinstance(obj, list):

            return [
                cls._expand_env(v)
                for v in obj
            ]

        if isinstance(obj, str):

            match = cls.ENV_PATTERN.fullmatch(
                obj
            )

            if match:

                return os.getenv(
                    match.group(1),
                    "",
                )

        return obj

    # --------------------------------------------------
    # Merge Defaults
    # --------------------------------------------------

    @classmethod
    def _merge_defaults(
        cls,
        defaults,
        custom,
    ):

        merged = defaults.copy()

        for key, value in custom.items():

            if (
                isinstance(value, dict)
                and key in merged
            ):

                merged[key] = (
                    cls._merge_defaults(
                        merged[key],
                        value,
                    )
                )

            else:

                merged[key] = value

        return merged

    # --------------------------------------------------
    # Convert Dictionary -> Config Model
    # --------------------------------------------------

    @classmethod
    def _to_model(
        cls,
        config,
    ):

        return RagoonConfig(

            llm=LLMConfig(
                **config["llm"]
            ),

            embedding=EmbeddingConfig(
                **config["embedding"]
            ),

            retrieval=RetrievalConfig(
                **config["retrieval"]
            ),

            chunking=ChunkingConfig(
                **config["chunking"]
            ),

            storage=StorageConfig(
                **config["storage"]
            ),

            data=DataConfig(
                **config["data"]
            ),
        )