from peewee import Model, SqliteDatabase, CharField, ForeignKeyField, DecimalField

db = SqliteDatabase('farm_bot.db')

class Section(Model):
    name = CharField(unique=True)

class Product(Model):
    name = CharField()
    description = CharField()
    section = ForeignKeyField(Section, backref='products')
    price = DecimalField(max_digits=10, decimal_places=2)
    photo_url = CharField()

db.connect()
db.create_tables([Section, Product], safe=True)
