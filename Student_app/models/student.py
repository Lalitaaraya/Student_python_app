class Student:
    def __init__(self, first_name, last_name, age, dob, email, phone, gender, course_name, middle_name=""):
        self.first_name = first_name
        self.middle_name = middle_name  # Optional
        self.last_name = last_name
        self.age = age
        self.dob = dob
        self.email = email
        self.phone = phone
        self.gender = gender
        self.course_name = course_name

    def to_dict(self):
        return {
            "First Name": self.first_name,
            "Middle Name": self.middle_name,
            "Last Name": self.last_name,
            "Age": self.age,
            "DOB": self.dob,
            "Email": self.email,
            "Phone": self.phone,
            "Gender": self.gender,
            "Course Name": self.course_name
        }
