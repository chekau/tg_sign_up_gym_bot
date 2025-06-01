import mysql.connector


connection = mysql.connector.connect(
    user='seschool_01',
    password='seschool_01',
    host='109.206.169.221',
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
        cursor = cls.cls.__conection.cursor()
        
        cursor.execute(sql, values)
        result = cls.__conection.cursor().fetchall()
        cls.__conection.commit()
        
        return result
    
    @classmethod
    def close(cls):
        cls.__conection.close()


class Client:
    @classmethod
    def add(cls,client: Client):
        sql = "INSERT INTO Client (`name`,`date_training`,`time_training`,`type_training`)  VALUE (%s, %s, %s, %s)"
        values = (client.name, client.date_training, client.time_training, client.type_training)
        Database.query(sql,values)
