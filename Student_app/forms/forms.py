from Validation.validators import (
    validate_name, validate_age, validate_dob, validate_email, validate_middle_name,
    validate_phone, validate_gender, validate_course, COURSES
)
from models.student import Student
from utils import save_student, count_students

def student_form():
    while True:
        try:
            first_name = validate_name(input("Enter First Name: "), field_name="First Name")
            middle_name = validate_middle_name(input("Enter Middle Name (optional): "), field_name="Middle Name", required=False)
            last_name = validate_name(input("Enter Last Name: "), field_name="Last Name")
            age = validate_age(input("Enter Age: "))
            dob = validate_dob(input("Enter Date of birth: "))
            email = validate_email(input("Enter Email: "))
            phone = validate_phone(input("Enter Phone Number: "))
            gender = validate_gender(input("Enter Gender (Male/Female/Other): "))

            print("\nAvailable Courses:")
            for idx, course in enumerate(COURSES, 1):
                print(f"{idx}. {course}")
            course_choice = int(input("Select Course by number: "))
            if course_choice < 1 or course_choice > len(COURSES):
                raise ValueError("Invalid course selection.")
            course_name = validate_course(COURSES[course_choice - 1])

            break
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.\n")

    student = Student(first_name, last_name, age, email, phone, gender, course_name, middle_name)
    save_student(student.to_dict())

    print(f"\nHello {student.first_name}!\n")
    print("You are registered. Here are your details:")
    for key, value in student.to_dict().items():
        print(f"{key}: {value}")
    
    total = count_students()
    print(f"\nTotal Registered Students: {total}")
