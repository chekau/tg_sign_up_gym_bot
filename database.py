import mysql.connector
from mysql.connector import Error

# Функция для создания соединения с MySQL
def create_connection(host_name, user_name, user_password, db_name=None):
    """Создает соединение с MySQL базой данных"""
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if conn.is_connected():
            print("Успешное подключение к базе данных")
    except Error as e:
        print(f"Ошибка '{e}' при подключении к базе данных")

    return conn

# Функция для создания базы данных
def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"База данных '{db_name}' успешно создана")
    except Error as e:
        print(f"Ошибка '{e}' при создании базы данных")

# Функция для создания таблицы клиентов
def create_clients_table(connection):
    cursor = connection.cursor()
    sql_create_clients_table = """
    CREATE TABLE IF NOT EXISTS clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        date_training DATETIME NOT NULL,
        time_training INT,
        type_training VARCHAR(15) NOT NULL,

    );
    """
    cursor.execute(sql_create_clients_table)
    print("Таблица 'clients' успешно создана")

# Функция для добавления нового клиента
def add_client(connection, name, date_training, time_training, type_training):
    """Добавляет нового клиента в таблицу клиентов"""
    sql = '''INSERT INTO clients(name, date_training, time_training, type_training)
              VALUES(%s, %s, %s, %s)'''
    cursor = connection.cursor()
    cursor.execute(sql, (name, date_training, time_training, type_training))
    connection.commit()
    print("Клиент успешно добавлен")
    return cursor.lastrowid

# Пример использования
if __name__ == '__main__':
    conn = create_connection('localhost', 'your_username', 'your_password')
    
    # Создаем базу данных
    create_database(conn, 'gym_bot')
    
    # Подключаемся к только что созданной базе данных
    conn.close()
    conn = create_connection('localhost', 'your_username', 'your_password', 'gym_bot')

    # Создаем таблицу клиентов
    create_clients_table(conn)
