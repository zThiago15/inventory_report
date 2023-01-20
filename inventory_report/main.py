import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return 'Verifique os argumentos'

    *_, path, report_type = sys.argv

    if ('csv' in path):
        return InventoryRefactor(CsvImporter).import_data(path, report_type)
    elif ('json' in path):
        return InventoryRefactor(JsonImporter).import_data(path, report_type)
    else:
        return InventoryRefactor(XmlImporter).import_data(path, report_type)
