import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @staticmethod
    def import_data(path: str, typeReport: str):
        if 'csv' in path:
            return Inventory.read_CSV(path, typeReport)
        elif 'json' in path:
            return Inventory.read_JSON(path, typeReport)

    @staticmethod
    def read_CSV(pathCSV: str, typeReport: str):
        with open(pathCSV, encoding="utf-8") as file:
            data = list(csv.DictReader(file, delimiter=",", quotechar='"'))

        return Inventory.generate_report(data, typeReport)

    @staticmethod
    def read_JSON(pathJSON, typeReport: str):
        with open(pathJSON) as file:
            data = json.loads(file.read())
        
        return Inventory.generate_report(data, typeReport)

    @staticmethod
    def read_JSON(pathJSON, typeReport: str):
        with open(pathJSON) as file:
            data = json.loads(file.read())
        
        return Inventory.generate_report(data, typeReport)

    @staticmethod
    def generate_report(data: list, typeReport: str):
        if (typeReport == 'simples'):
            return SimpleReport.generate(data)

        return CompleteReport.generate(data)


print(Inventory.import_data('inventory_report/data/inventory.json', 'completo'))
