from courses import Course
from student import Student


def main():

    #
    courses = Course()
    if courses.course_file_exists():
        pass
    else:
        courses.save_data()

    student = Student()
    student.display_home_page()

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1 or choice == 2:
            student.process_home_choice(choice)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
