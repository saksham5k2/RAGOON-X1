from .checks import DoctorChecks
from .report import DoctorReport


class Doctor:

    @staticmethod
    def run():

        print("\nRAGOON-X1 Diagnostics\n")

        checks = [

            (
                "Configuration",
                DoctorChecks.config_exists(),
            ),

            (
                "GROQ API Key",
                DoctorChecks.groq_key(),
            ),

            (
                "Qdrant Storage",
                DoctorChecks.qdrant_exists(),
            ),

            (
                "BM25 Index",
                DoctorChecks.bm25_exists(),
            ),

            (
                "Document Store",
                DoctorChecks.documents_exist(),
            ),

        ]

        passed = 0

        for name, result in checks:

            DoctorReport.print_check(
                name,
                result,
            )

            if result:

                passed += 1

        print(
            f"\n{passed}/{len(checks)} checks passed."
        )