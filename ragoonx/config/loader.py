import os
import re
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

    @classmethod
    def load(
        cls,
        path="ragoonx/config/defaults.yaml",
    ):

        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        config = cls._expand_env(config)

        config = cls._merge_defaults(
            DEFAULT_CONFIG,
            config,
        )

        return cls._to_model(config)

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

            match = cls.ENV_PATTERN.fullmatch(obj)

            if match:

                return os.getenv(
                    match.group(1),
                    "",
                )

        return obj

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

                merged[key] = cls._merge_defaults(
                    merged[key],
                    value,
                )

            else:

                merged[key] = value

        return merged

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