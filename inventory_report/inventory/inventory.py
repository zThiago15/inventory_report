import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @staticmethod
    def import_data(pathCSV: str, typeReport: str):
        with open(pathCSV, encoding="utf-8") as file:
            data = list(csv.DictReader(file, delimiter=",", quotechar='"'))

        if (typeReport == 'simples'):
            return SimpleReport.generate(data)

        return CompleteReport.generate(data)


# print(Inventory.import_data('inventory_report/data/inventory.csv', 'completo'))