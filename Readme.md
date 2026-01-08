# Student Python App

A Python project for managing student data with a modular structure including forms, models, and validation.

## Project Structure

STUDENT_APP/
├── storage/
│ └── students.csv
├── Student_app/
│ ├── pycache/
│ ├── forms/
│ ├── models/
│ ├── Validation/
│ ├── init.py
│ ├── main.py
│ └── utils.py
├── .vscode/
├── Readme.md
└── requirements.txt

yaml
Copy code

- **storage/**: Contains CSV files for student data.
- **Student_app/**: Core application code.
  - **forms/**: Input forms for student data.
  - **models/**: Data models for the application.
  - **Validation/**: Validation logic for inputs.
  - **main.py**: Entry point of the application.
  - **utils.py**: Helper functions.
- **requirements.txt**: Python dependencies.
- **Readme.md**: Project documentation.

## Setup and Running

1. **Clone the repository:**

```bash
git clone https://github.com/Lalitaaraya/Student_python_app.git
cd Student_python_app
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
cd Student_app
python main.py
Notes
Ensure Python 3.8+ is installed.

The application reads and writes student data from storage/students.csv.

Modify or add forms, models, or validation rules as needed.
