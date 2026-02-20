CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students 
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    marks INT
);
