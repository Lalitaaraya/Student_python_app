# Student Registration Console App

A simple console-based Python app to register students with strict validation and CSV storage.

## Features

- Collects the following information:
  - First Name (required)
  - Middle Name (optional)
  - Last Name (required)
  - Age (required, 5-120)
  - Email (required, valid format)
  - Phone (required, 10 digits)
  - Gender (required, Male/Female/Other)
  - Course Name (required, choose from predefined courses)
- Strict validation for all required fields.
- Optional Middle Name field.
- Saves student data to a CSV file (`students.csv`).
- Displays total registered students.

## Predefined Courses

- Mathematics
- Physics
- Chemistry
- Biology
- Computer Science
- English

## Project Structure

STUDENT_APP/
│
├── storage/
│   └── students.csv         # Stores student data
├── Student_app/
│   ├── forms/
│   │   └── forms.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   ├── validation/
│   │   ├── __init__.py
│   │   └── validators.py
│   ├── main.py
│   └── utils.py
├── .vscode/
├── README.md
└── requirements.txt

## How to Run

1. Clone the repository or download the project.
2. Ensure you have Python 3.8+ installed.
3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

<<<<<<< HEAD:README.md
<<<<<<< HEAD:Readme.md
##NOTE- Change the Direcory before running main.py file
=======
NOTE- Change directory before running
>>>>>>> ca8e46f (Update README.md):README.md
cd Student_app
python main.py
Follow the prompts to register a student.
=======
4. Install dependencies:
>>>>>>> 934dcf92b9fb86fc2643a113445cd1cc493da59a:Readme.md

    ```bash
    pip install -r requirements.txt
    ```

5. Run the app:

    ```bash
    # Change directory before running
    cd Student_app
    python main.py
    ```

6. Follow the prompts to register a student.

## Notes

- CSV file (`students.csv`) is automatically created in the `storage` folder if it doesn’t exist.
- Only valid course names can be selected.
- Middle Name is optional.
