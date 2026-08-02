import csv


class ExportService:

    @staticmethod
    def export(history):

        with open(
            "history.csv",
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Expression",
                    "Result",
                    "Timestamp",
                ]
            )

            writer.writerows(history)