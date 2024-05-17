import mysql.connector

# Database connection details
host = "127.0.0.1"
user = "root"
password = "root"
database = "carrental"

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=host,  
            user=user,
            password=password,
            database=database
        )
        return connection
    except mysql.connector.Error as error:
        print(f"Error connecting to the database: {error}")
        return None