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


    @classmethod
    def query(cls, sql, values):
        cursor = cls.__conection.cursor()
        
        cursor.execute(sql, values)
        result = cls.__conection.cursor().fetchall()
        cls.__conection.commit()
        
        return result
    
    @classmethod
    def close(cls):
        cls.__conection.close()




class TrainingTable:
    @classmethod
    def add(cls,training: Training):
        sql = "INSERT INTO Training (`date_training`,`time_training`,`type_training`) VALUE (%s,%s,%s)"
        values = [training.date_training, training.time_training, training.type_training]
        Database.query(sql,values)

    # @classmethod
    # def create(cls,training: Training):
    #     sql = "CREATE TABLE Training (`date_training` DATETIME, `time_training` DATETIME, `type_training` VARCHAR(100))"




class ClientTable:
    @classmethod
    def add(cls, name, phone_number):
        sql = "INSERT INTO Сlient_gym (`name`,`phone_number`)  VALUE (%s, %s)"
        values = (name, phone_number)
        Database.query(sql,values)
