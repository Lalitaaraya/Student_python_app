# Student Python App

A modular Python application to manage student data with validation and forms.  

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This project manages student information using a modular Python structure. It includes models, forms, validation, and utility functions for CRUD operations.  

---

## Features

- Add new students
- Update student details
- Delete student records
- Save and load student data from CSV
- Modular Python code for maintainability
- Input validation for data consistency

---

## Project Structure

STUDENT_APP/
│
├── storage/
│ └── students.csv # Persistent storage for student data
├── Student_app/
│ ├── forms/
│ │ └── forms.py # Input forms for student data
│ ├── models/
│ │ ├── init.py
│ │ └── student.py # Student data model
│ ├── validation/
│ │ ├── init.py
│ │ └── validators.py # Input validation functions
│ ├── main.py # Entry point of the application
│ └── utils.py # Utility functions like file operations
├── .vscode/ # VSCode workspace settings
├── Readme.md # Project documentation
└── requirements.txt # Python dependencies

The project is organized into several folders and files for modularity and clarity:

storage/ – Contains students.csv, the file where all student data is stored persistently.

Student_app/ – Main application folder:

forms/ – Contains forms.py, which defines input forms for student data.

models/ – Contains student.py defining the Student data model and __init__.py.

validation/ – Contains validators.py for input validation and __init__.py.

main.py – Entry point of the application, providing the menu interface.

utils.py – Utility functions like reading/writing CSV files or helper functions.

.vscode/ – VSCode workspace settings (optional).

Readme.md – Project documentation.

requirements.txt – Python dependencies for the project.

This structure ensures separation of concerns: models handle data, forms handle input, validation ensures correctness, and utilities manage file operations.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Lalitaaraya/Student_python_app.git
cd STUDENT_APP
(Optional) Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Navigate to the Student_app folder and run the main file:

bash
Copy code
cd Student_app
python main.py

Notes
Ensure students.csv exists in the storage/ folder before running the app.

All changes are saved to the CSV file automatically.

Modify forms, models, or validators to extend the app functionality.

Contributing
Fork the repository

Create a new branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/YourFeature)

Create a Pull Request
