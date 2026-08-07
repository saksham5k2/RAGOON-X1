from colorama import (
    Fore,
    Style,
    init,
)

init(autoreset=True)


class DoctorReport:

    @staticmethod
    def print_header():

        print(
            f"{Fore.CYAN}"
            "\n"
            "────────────────────────────────\n"
            "RAGOON-X1 Diagnostics\n"
            "────────────────────────────────\n"
        )

    @staticmethod
    def print_check(
        name,
        passed,
        fix=None,
    ):

        if passed:

            print(
                f"{Fore.GREEN}✓ {name}"
            )

        else:

            print(
                f"{Fore.RED}✗ {name}"
            )

            if fix:

                print(
                    f"  {Fore.YELLOW}{fix}"
                )

    @staticmethod
    def print_summary(
        passed,
        total,
    ):

        print(
            f"\n{Fore.CYAN}"
            "────────────────────────────────"
        )

        if passed == total:

            print(
                f"{Fore.GREEN}"
                "Framework Healthy ✓"
            )

        else:

            print(
                f"{Fore.YELLOW}"
                f"{passed}/{total} checks passed."
            )

        print(
            f"{Fore.CYAN}"
            "────────────────────────────────"
        )