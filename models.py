from peewee import *
import datetime
db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db

class File(BaseModel):
	id = IntegerField(primary_key = True)
	name = CharField()

File.create_table()	

