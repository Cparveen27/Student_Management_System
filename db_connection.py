import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cparveen$123",
            database="student_db"
        )

        if conn.is_connected():
            print("Connected to MySQL successfully!")
            return conn

    except Error as e:
        print("Error while connecting:", e)
        return None

if __name__ == "__main__":
    connection = connect_db()
