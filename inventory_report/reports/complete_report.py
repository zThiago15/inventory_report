from inventory_report.reports.simple_report import SimpleReport
from collections import defaultdict


class CompleteReport(SimpleReport):

    def products_per_company(list_products):
        companies = defaultdict(int)

        for product in list_products:
            companies[product['nome_da_empresa']] += 1

        return companies

    @staticmethod
    def generate(list_products):
        companies_count = CompleteReport.products_per_company(list_products)

        output = SimpleReport.generate(list_products)

        output += "\nProdutos estocados por empresa:\n"

        for company, count in companies_count.items():
            output += f"- {company}: {count}\n"

        return output
