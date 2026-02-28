# performing mysql CRUD operations

from db_connection import connect_db
from models import Student1

def execute_query(query, params=None, fetch=False, single=False):
    conn = connect_db()
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchone() if single else cursor.fetchall()
        conn.commit()
    except Exception as e:
        print("Database Error:", e)
    finally:
        cursor.close()
        conn.close()


def add_student():
    print("\n--- Add New Student ---")
    try:
        name = input("Name: ").strip()
        age = int(input("Age: "))
        gender = input("Gender: ").strip()
        course = input("Course: ").strip()
        marks = float(input("Marks: "))

        query = "INSERT INTO student1(name, age, gender, course, marks) VALUES (%s,%s,%s,%s,%s)"
        execute_query(query, (name, age, gender, course, marks))
        print("Student Added Successfully!")
    except ValueError:
        print("Invalid input! Age and Marks must be numbers.")


def view_students():
    records = execute_query("SELECT * FROM student1", fetch=True)
    if not records:
        print("No student records found. Please add students first!")
        return
    print("\n--- Student List ---")
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Gender':<10} {'Course':<15} {'Marks':<6}")
    print("-"*65)
    for row in records:
        s = Student1(*row)
        print(f"{s.id:<5} {s.name:<20} {s.age:<5} {s.gender:<10} {s.course:<15} {s.marks:<6}")


def search_by_id():
    try:
        sid = int(input("Enter Student ID to search: "))
        record = execute_query("SELECT * FROM student1 WHERE id=%s", (sid,), fetch=True, single=True)
        if record:
            s = Student1(*record)
            print("\n--- Student Found ---")
            print(s)
        else:
            print("Student not found!")
    except ValueError:
        print("Invalid input! ID must be a number.")


def update_student():
    try:
        sid = int(input("Enter Student ID to update: "))
        new_marks = float(input("Enter New Marks: "))
        execute_query("UPDATE student1 SET marks=%s WHERE id=%s", (new_marks, sid))
        print("Student Marks Updated Successfully!")
    except ValueError:
        print("Invalid input! ID and Marks must be numbers.")


def delete_student():
    try:
        sid = int(input("Enter Student ID to delete: "))
        execute_query("DELETE FROM student1 WHERE id=%s", (sid,))
        print("Student Deleted Successfully!")
    except ValueError:
        print("Invalid input! ID must be a number.")


def display_topper():
    record = execute_query("SELECT * FROM students ORDER BY marks DESC LIMIT 1", fetch=True, single=True)
    if record:
        s = Student1(*record)
        print("\n Top Scorer:")
        print(s)
    else:
        print("No student records found. Please add students first!")
