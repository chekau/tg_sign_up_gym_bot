import mysql.connector
from model import Client,Training


connection = mysql.connector.connect(
    
    host='109.206.169.221',
    user='seschool_01',
    password='seschool_01',
    database='seschool_01_pks1'
)

class Database: 
    __conection = None
    @classmethod
    def open(cls, 
             host='109.206.169.221', 
             user='seschool_01', 
             password='seschool_01', 
             database='seschool_01_pks1'):
        if cls.__conection is None:
            cls.__conection = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database   
            )

            cls.__cursor = cls.__conection.cursor()
    @classmethod
    def query(cls, sql, values):

        cls.__cursor.execute(sql,values)
        cls.__conection.commit()
        result = cls.__cursor.fetchall()
        return result   
    @classmethod
    def close(cls):
        cls.__conection.close()

class TrainingTable:
    @classmethod
    def add(cls,date_training, time_training, type_training):
        sql = "INSERT INTO Training (`date_training`,`time_training`,`type_training`) VALUE (%s,%s,%s)"
        values = (date_training, time_training, type_training)
        Database.query(sql,values)

class ClientTable:
    @classmethod
    def add(cls, name, phone_number):
        sql = "INSERT INTO Client_gym (`name`,`phone_number`)  VALUE (%s, %s)"
        values = (name, phone_number)
        Database.query(sql,values)
