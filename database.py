# ṃysql connection setup
import mysql.connector
# database credential
def get_connection():
    try:
        connection = mysql.connector.connect
        (
            host="localhost",
            user="root",
            password="your_password",
            database="student_db"
        )
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)
    
#create database
CREATE DATABASE student_db;
USE student_db;

# create table
CREATE TABLE students 
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) Not Null,
    age INT Not Null,
    course VARCHAR(100),
    marks FLOAT Not Null
)
