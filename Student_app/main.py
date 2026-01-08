from forms.forms import student_form
from utils import count_students

def main():
    print("Welcome to Student Registration App\n")
    while True:
        student_form()
        choice = input("\nDo you want to register another student? (y/n): ").strip().lower()
        if choice != 'y':
            total_registered = count_students()
            print(f"\nTotal students registered so far: {total_registered}")
            print("Thank you for using the registration app!")
            break

if __name__ == "__main__":
    main()

