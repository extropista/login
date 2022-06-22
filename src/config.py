#from src import app
from src.__init__ import app
from flask_mysqldb import MySQL
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect



#Parametros de Conección a DB

db = MySQL(app)

class Config:
    SECRET_KEY = '4HfN%5ZNe5tDH@vi&^*gSJ5E'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Z#8mbprL4FQg%J7m$Dh2'
    MYSQL_DB = 'fundacionayuda'

default_config = {
    'development': DevelopmentConfig
}



# Protección AJAX (globalmente) para solicitudes de vistas

csrf = CSRFProtect()