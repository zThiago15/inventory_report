from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if 'json' not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            return json.loads(file.read())
