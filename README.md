# 🎓 Student Management System

A console-based application built using **Python and MySQL** to manage student records efficiently through CRUD operations.

---

## 📌 Project Overview

The Student Management System allows users to perform core database operations such as creating, reading, updating, and deleting student records. It demonstrates practical implementation of database connectivity, structured SQL queries, and backend logic using Python.

---

## 🚀 Key Features

- Add new student records
- View all student details
- Search student by ID
- Update student information
- Delete student records
- Auto-incremented unique student ID
- Secure parameterized SQL queries
- Structured and modular code

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 3 | Application logic and user interaction |
| MySQL | Database for storing student records |
| mysql-connector-python | Connects Python with MySQL |
| SQL | Performs CRUD operations |

---

## 🗄 Database Schema

Table: `students`

| Column  | Type  | Description |
|---------|-------|------------|
| id      | INT (PK, AUTO_INCREMENT) | Unique Student ID |
| name    | VARCHAR(100) | Student Name |
| age     | INT | Student Age |
| course  | VARCHAR(100) | Course Name |
| marks   | FLOAT | Student Marks |

---

## ⚙ Installation & Setup

### 1️⃣ Create Database

```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks FLOAT
);
```

## 2️⃣ Install Required Library
----
pip install mysql-connector-python

---

## 3️⃣ Configure Database Credentials

host="localhost"
user="root"
password="your_password"
database="student_db"

---

## 4️⃣ Run the Application

python main.py

---
