import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="student_db"
    )
    return connection
