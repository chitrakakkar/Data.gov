'''This is where the peewee model for a job will be stored'''

from peewee import *

import os
# for subdir, dirs, files in os.walk('./'):
#     if "CK.db" in files:
#       os.remove("CK.db")


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


