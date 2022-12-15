import datetime


class SimpleReport:
    # def __init__(self) -> None:
    #     pass

    @staticmethod
    def company_with_more_products(products):
        companies = {}

        for product in products:

            current_company = product['nome_da_empresa']
            if current_company not in companies:
                companies[current_company] = 1
            else:
                companies[current_company] += 1

        max_company = max(companies, key=companies.get)
        return max_company

    @staticmethod
    def generate(list_products):
        ancient_fabrication = list_products[0]['data_de_fabricacao']
        recent_validity = list_products[0]['data_de_validade']
        current_date = str(datetime.datetime.now().date())

        for product in list_products:

            current_fabrication = product['data_de_fabricacao']
            if current_fabrication < ancient_fabrication:
                ancient_fabrication = current_fabrication

            current_validity = product['data_de_validade']
            if (
                current_validity < recent_validity
                and current_validity > current_date
            ):
                recent_validity = current_validity

        max_company = SimpleReport.company_with_more_products(list_products)

        return (
            f"Data de fabricação mais antiga: {ancient_fabrication}\n"
            f"Data de validade mais próxima: {recent_validity}\n"
            f"Empresa com mais produtos: {max_company}"
        )
