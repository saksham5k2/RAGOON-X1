import argparse

from .core.ragoon import Ragoon
from .config import ConfigLoader


def main():

    parser = argparse.ArgumentParser(
        prog="ragoonx",
        description="RAGOON-X1 CLI",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    subparsers.add_parser(
        "chat",
        help="Start interactive chat",
    )

    subparsers.add_parser(
        "ingest",
        help="Run document ingestion",
    )

    subparsers.add_parser(
        "init",
        help="Create ragoonx.yaml",
    )

    subparsers.add_parser(
        "doctor",
        help="Run diagnostics",
)

    args = parser.parse_args()

    if args.command == "init":

        ConfigLoader.initialize()

        return

    if args.command == "doctor":

        from .doctor import Doctor
        Doctor.run()
        return

    rag = Ragoon()

    try:

        if args.command == "chat":

            rag.chat()

        elif args.command == "ingest":

            rag.ingest()

        else:

            parser.print_help()

    finally:

        rag.close()


if __name__ == "__main__":

    main()