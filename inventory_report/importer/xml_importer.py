from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if 'xml' not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            return xmltodict.parse(file.read())['dataset']['record']
