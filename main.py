from student import Student


def main():
    student = Student(
        student_number='',
        national_code='',
        first_name='',
        last_name='',
        gender='',
        marital_status='',
        phone_number='',
        mothers_name='',
        fathers_name='',
        address='',
        tuition_based_or_free='',
        faculty_name='',
        field_of_study=''
    )

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
