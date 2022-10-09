from peewee import *
from decouple import config


database = MySQLDatabase(
    config('MYSQL_DB'),
    user=config('MYSQL_USER'), 
    password=config('MYSQL_PASSWORD'),
    host=config('MYSQL_HOST'), 
    port=config('MYSQL_PORT')
)

class User(Model):
    username = CharField(max_length=50)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'
