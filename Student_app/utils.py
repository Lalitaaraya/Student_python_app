import csv
import os

STORAGE_FILE = os.path.join(os.path.dirname(__file__), '../storage/students.csv')

def save_student(student_dict):
    file_exists = os.path.isfile(STORAGE_FILE)
    with open(STORAGE_FILE, 'a', newline='') as csvfile:
        fieldnames = ["First Name", "Last Name", "Age", "Email", "Phone", "Gender", "Course Name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(student_dict)

def count_students():
    if not os.path.isfile(STORAGE_FILE):
        return 0
    with open(STORAGE_FILE, 'r') as csvfile:
        return sum(1 for row in csvfile) - 1  # subtract header