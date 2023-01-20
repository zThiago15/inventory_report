import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    pass
    if len(sys.argv) < 3:
        sys.stderr.write('Verifique os argumentos\n')
        return

    *_, path, report_type = sys.argv

    report = ''
    if ('.csv' in path):
        report = InventoryRefactor(CsvImporter).import_data(path, report_type)
    elif ('.json' in path):
        report = InventoryRefactor(JsonImporter).import_data(path, report_type)
    elif ('.xml' in path):
        report = InventoryRefactor(XmlImporter).import_data(path, report_type)
    else:
        raise ValueError('invalid extension file')

    print(report, end="")


if __name__ == "__main__":
    main()
