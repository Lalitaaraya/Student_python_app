import re

COURSES = ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "English"]

# Validation functions (from your code)
def validate_name(name, field_name="Name", required=True):
    name = name.strip()
    if required and not name:
        raise ValueError(f"{field_name} cannot be empty.")
    if name and (not name.isalpha() or len(name) < 2):
        raise ValueError(f"{field_name} must contain only letters and be at least 2 characters long.")
    return name.title()

def validate_middle_name(name):
    name = name.strip()
    if name:  # Only validate if user enters something
        if not name.isalpha() or len(name) < 2:
            raise ValueError("Middle Name must contain only letters and be at least 2 characters long.")
        return name.title()
    return ""  # Return empty string if no middle name

def validate_age(age):
    age = int(age)
    if age < 5 or age > 120:
        raise ValueError("Age must be between 5 and 120.")
    return age

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format.")
    return email.lower()

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone number must be 10 digits.")
    return phone

def validate_gender(gender):
    gender = gender.strip().capitalize()
    if gender not in ["Male", "Female", "Other"]:
        raise ValueError("Gender must be Male, Female, or Other.")
    return gender

def validate_course(course_name):
    course_name = course_name.strip().title()
    if not course_name:
        raise ValueError("Course Name cannot be empty.")
    if course_name not in COURSES:
        raise ValueError(f"Course must be one of: {', '.join(COURSES)}")
    return course_name

# Store all registered students
registered_students = []

def register_student():
    try:
        first_name = validate_name(input("Enter First Name: "), "First Name")
        middle_name = validate_middle_name(input("Enter Middle Name (optional): "))
        last_name = validate_name(input("Enter Last Name: "), "Last Name")
        age = validate_age(input("Enter Age: "))
        email = validate_email(input("Enter Email: "))
        phone = validate_phone(input("Enter Phone (10 digits): "))
        gender = validate_gender(input("Enter Gender (Male/Female/Other): "))
        course = validate_course(input(f"Enter Course {COURSES}: "))

        student = {
            "First Name": first_name,
            "Last Name": last_name,
            "Age": age,
            "Email": email,
            "Phone": phone,
            "Gender": gender,
            "Course": course
        }

        registered_students.append(student)

        # Print the confirmation
        print(f"\nHello {first_name}!\n")
        print("You are registered. Below are your details:\n")
        for key, value in student.items():
            print(f"{key}: {value}")
        
        print(f"\nTotal registered students: {len(registered_students)}\n")

    except ValueError as ve:
        print(f"Error: {ve}\nPlease try again.\n")
        register_student()  # Retry registration

# Example: register 1 student
register_student()
