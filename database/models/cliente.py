from peewee import Model, CharField, DateTimeField
from database.database import db
from datetime import datetime

# Define uma função que retorna o tempo atual
def current_time():
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y %H:%M")
    return formatted_date

class Person(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=current_time)

    class Meta:
        database = db