from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    list_product = [{
        "id": "1",
        "nome_do_produto": "notebook lenovo i7",
        "nome_da_empresa": "Lenovo",
        "data_de_fabricacao": "2010-03-27",
        "data_de_validade": "2030-11-29",
        "numero_de_serie": "AFDS2384HDFS",
        "instrucoes_de_armazenamento": "Manter em local fechado",
    }]

    simple_report = ColoredReport(SimpleReport).generate(list_product)
    assert (
        "\033[31mLenovo\033[0m" in simple_report
    ) is True

    assert (
        "\033[32mData de fabricação mais antiga:\033[0m" in simple_report
    ) is True
    
    assert (
        "\033[36m2010-03-27\033[0m" in simple_report
    ) is True

    complete_report = ColoredReport(SimpleReport).generate(list_product)

    assert (
        "\033[31mLenovo\033[0m" in complete_report
    ) is True

    assert (
        "\033[32mData de fabricação mais antiga:\033[0m" in complete_report
    ) is True
    
    assert (
        "\033[36m2010-03-27\033[0m" in complete_report
    ) is True
