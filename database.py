#create database
CREATE DATABASE student_db;
USE student_db;

# create table
CREATE TABLE student1
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) Not Null,
    age INT Not Null,
    gender VARCHAR(10),
    course VARCHAR(100),
    marks FLOAT Not Null
)
