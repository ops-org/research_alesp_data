from peewee import *
from playhouse.db_url import connect

db = MySQLDatabase("ops_despesas_sp", host='127.0.0.1', user='root', password='302010')


class Despesa(Model):
    deputado = CharField(max_length=254, null=True)
    matricula = CharField(max_length=254,null=True)
    ano = IntegerField(null=True)
    mes = IntegerField(null=True)
    tipo = CharField(max_length=254, null=True)
    cnpj = CharField(max_length=254, null=True)
    fornecedor = CharField(max_length=254, null=True)
    valor = FloatField(null=True)

    class Meta:
        database = db  # This model uses the "people.db" database.


if __name__ == '__main__':
    print ('Creating tables...')
    db.create_table(Despesa)
