from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.data = []
        self.importer = importer

    def import_data(self, file_path, report_type):
        self.data += self.importer.import_data(file_path)

        if (report_type == 'simples'):
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
