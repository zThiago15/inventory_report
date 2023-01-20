from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if 'csv' not in path:
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            return list(csv.DictReader(file, delimiter=",", quotechar='"'))
