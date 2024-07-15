print("\n---Student Grade Management System---\n")
def grading_scheme():
   
    print("1.Add Student")
    print("2.Update Student")
    print("3.Delete Student")
    print("4.View Student")
    print("5.Exit")

def user_choice():
    return input("Enter your choice: ")

grades = {} #Dictionary for store Student Grades

def add_student(): #1.Add Student Name With Marks
    s_name = input("Enter Student Name: ").capitalize()
    s_marks = int(input("Enter Student marks: "))
    grades[s_name] = s_marks
    print(f"Student {s_name} added with grade {s_marks}.")

def update_student(): #2.Update Student Marks
    s_name = input("Enter Student Name Whose Marks You Want To Update: ").capitalize()
    if s_name in grades:
        new_marks = int(input("Enter New Marks: "))
        grades[s_name] = new_marks
        print(f"Student name {s_name} marks are updated successfully.")
    else:
        print("Please Enter Valid Student Name.") 

def delete_student(): #3.Delete Student
    s_name = input("Enter Student Name You Want To Delete: ").capitalize()
    if s_name in grades:
        del grades[s_name]
        print(f"Student Name {s_name} Deleted Successfully.")
    else:
        print(f"Student {s_name} not in the System.")

def view_student(): #4.View Total Students
    print(f"Total Students are: {grades}")


def main():
    while True:
        grading_scheme() #Call the function
        operation = user_choice()

        if operation == '1':
            add_student()
        elif operation == '2':
            update_student()
        elif operation == '3':
            delete_student()
        elif operation == '4':
            view_student()
        elif operation == '5':
            print("---Application Closed---")
            break
        else:
            print("Invaid Choice. Please Try Again!")


if __name__ == "__main__":
    main()            

############################################################################################
#ChatGpt Version
print("\n---Student Grade Management System---\n")

def grading_scheme():
    """Display the grading scheme options."""
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View Student")
    print("5. Exit")

def user_choice():
    """Prompt the user to enter their choice."""
    return input("Enter your choice: ")

grades = {}  # Dictionary to store student grades

def add_student():
    """Add a student name with marks."""
    s_name = input("Enter student name: ").capitalize()
    try:
        s_marks = int(input("Enter student marks: "))
        grades[s_name] = s_marks
        print(f"Student {s_name} added with grade {s_marks}.")
    except ValueError:
        print("Invalid marks. Please enter an integer value.")

def update_student():
    """Update student marks."""
    s_name = input("Enter student name whose marks you want to update: ").capitalize()
    if s_name in grades:
        try:
            new_marks = int(input("Enter new marks: "))
            grades[s_name] = new_marks
            print(f"Student {s_name}'s marks are updated successfully.")
        except ValueError:
            print("Invalid marks. Please enter an integer value.")
    else:
        print("Please enter a valid student name.")

def delete_student():
    """Delete a student."""
    s_name = input("Enter student name you want to delete: ").capitalize()
    if s_name in grades:
        del grades[s_name]
        print(f"Student {s_name} deleted successfully.")
    else:
        print(f"Student {s_name} not in the system.")

def view_student():
    """View total students and their grades."""
    if grades:
        for s_name, s_marks in grades.items():
            print(f"{s_name}: {s_marks}")
    else:
        print("No students in the system.")

def main():
    """Main function to run the student grade management system."""
    while True:
        grading_scheme()  # Call the function
        operation = user_choice()

        if operation == '1':
            add_student()
        elif operation == '2':
            update_student()
        elif operation == '3':
            delete_student()
        elif operation == '4':
            view_student()
        elif operation == '5':
            print("---Application Closed---")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()

