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


# data = [
#   {
#     "id": 1,
#     "nome_do_produto": "MESA",
#     "nome_da_empresa": "Forces of Nature",
#     "data_de_fabricacao": "2022-05-04",
#     "data_de_validade": "2023-02-09",
#     "numero_de_serie": "FR48",
#     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
#   }
# ]

# print(CompleteReport.generate(data))
