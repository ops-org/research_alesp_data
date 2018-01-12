import xml.etree.ElementTree as ET
from models import Despesa

tree = ET.parse('despesas_gabinetes.xml')
root = tree.getroot()

counter = 0
for item in root:
    if counter > 443114:
        deputado = item.find('Deputado').text
        matricula = item.find('Matricula').text
        ano = item.find('Ano').text
        mes = item.find('Mes').text
        tipo = item.find('Tipo').text
        cnpj = item.find('CNPJ').text if item.find('CNPJ') else None
        fornecedor = item.find('Fornecedor').text
        valor = item.find('Valor').text

        Despesa(
            deputado=deputado,
            matricula=matricula,
            ano=ano,
            mes=mes,
            tipo=tipo,
            cnpj=cnpj,
            fornecedor=fornecedor,
            valor=valor
        ).save()

        print (f"{counter} - {deputado} - {ano}/{mes} - R$ {valor}")
    else:
        print (f"{counter} - skip")

    counter += 1