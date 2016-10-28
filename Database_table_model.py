

'''This is where the peewee model for a book will be stored'''
from peewee import *

"""Make sure that this object stores the goodreads _id.  We will need it later.
    https://www.goodreads.com/search/index.xml?q=Ender&key=4ylN8OWi1dhG5Yhq3PQstA
    that will show you what types of data the server responds with."""

db = SqliteDatabase("CK.db")


class Base_Model(Model):
    class Meta:
        database = db


class job_table_model(Base_Model):
    Job_ID = CharField(max_length=60, unique=True)
    Job_Title = CharField(max_length=120)
    Company_Name = CharField(max_length=100)
    Salary = CharField(max_length=100)
    Last_Date = CharField(max_length=100)
    Location = CharField(max_length=100)
    Link = CharField(max_length=100)


