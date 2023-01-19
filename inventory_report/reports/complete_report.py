from simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(list_products):
        simple_report = super().generate(list_products)
        print(simple_report)


print(CompleteReport.generate())
