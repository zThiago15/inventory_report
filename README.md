# Projeto Inventory Report 📝

## Introdução 📜
 Este é um gerador de relatórios que recebe como entrada arquivos com dados de um estoque. Os formatos podem ser CSV, JSON e XML. A partir desses dados, é gerado como saída um relatório. Pode ser gerado dois tipos de relatórios:
 
 > Relatório simples
 
```
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
```
 
 > Relatório completo
 
```
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```

## Requerimentos 📋

- Python 3.x
- Xmltodict

## Instalação 🚀

1. Clone o repositório: `git clone https://github.com/zThiago15/inventory-report.git`
2. Vá para o diretório: `cd inventory-report`
3. Instale os pacotes necessários: `pip install -r requirements.txt`

## Uso 🔧

- Abra um terminal interativo do Python: `python3 -i inventory_report/reports/simple_report.py`
- Execute o método `generate` da classe SimpleReport no caminho `inventory_report/reports/simple_report.py`

## Contribuição 🙏

Se você deseja contribuir com o projeto, por favor, faça um fork do repositório e envie uma pull request.

## Contato 📧

Se você tiver alguma dúvida ou sugestão, por favor, sinta-se a vontade para entrar em contato comigo pelo e-mail: thiagodias.db15@gmail.com
