import pickle
import courses
import datetime
import random


class Person:
    def __init__(self, national_code, first_name, last_name):
        self.national_code = national_code
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, student_number, national_code, first_name, last_name, gender, marital_status,
                 phone_number, mothers_name, fathers_name, address, tuition_based_or_free, faculty_name,
                 field_of_study):
        super().__init__(national_code, first_name, last_name)
        self.student_number = student_number
        self.gender = gender
        self.marital_status = marital_status
        self.phone_number = phone_number
        self.mothers_name = mothers_name
        self.fathers_name = fathers_name
        self.address = address
        self.tuition_based_or_free = tuition_based_or_free
        self.faculty_name = faculty_name
        self.field_of_study = field_of_study
        self.login_time = None
        self.logout_time = None

    def display_course_data(self):
        students = Student.load_student_data()

        if self.student_number in students:
            student_data = students[self.student_number]
            if "courses" in student_data:
                print("Courses:")
                for course_id, course_info in student_data["courses"].items():
                    print("-" * 20)
                    print(f"Course ID: {course_id}")
                    print(f"Course Name: {course_info['course_name']}")
                    print(f"Professor Name: {course_info['prof_name']}")
                    # print()
                print("-" * 20)
            else:
                print("No courses found for this student.")
            print()
        else:
            print("Student data not found.")

    @staticmethod
    def load_student_data():
        try:
            with open("student_data.pickle", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_student_data(data):
        with open("student_data.pickle", "wb") as file:
            pickle.dump(data, file)

    @staticmethod
    def load_course_data():
        try:
            with open("courses.pickle", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

    def assign_money(self):
        student_data = Student.load_student_data()
        if self.student_number in student_data:
            student = student_data[self.student_number]
            student['financial_id'] = {'budget': random.randint(0, 2000)}
            student_data[self.student_number] = student
            Student.save_student_data(student_data)
        return student_data

    @staticmethod
    def display_home_page():
        print("Welcome to the Student Online System!")
        print("1. Login")
        print("2. Register")

    def process_home_choice(self, choice):
        if choice == 1:
            self.login()
        elif choice == 2:
            self.register()
        else:
            print("Invalid choice. Please try again.")

    def load_student(self, students, student_number):
        if student_number in students:
            student_data = students[student_number]
            self.student_number = student_number
            self.national_code = student_data["national_code"]
            self.first_name, self.last_name = student_data["name"].split(" ")
            self.gender = student_data["gender"]
            self.marital_status = student_data["marital_status"]
            self.phone_number = student_data["phone_number"]
            self.mothers_name = student_data["mothers_name"]
            self.fathers_name = student_data["fathers_name"]
            self.address = student_data["address"]
            self.tuition_based_or_free = student_data["tuition_based_or_free"]
            self.faculty_name = student_data["faculty_name"]
            self.field_of_study = student_data["field_of_study"]
            return True
        else:
            return False

    def display_student_info(self):
        students = Student.load_student_data()
        if self.student_number in students:
            student_data = students[self.student_number]
            print("About {}:".format(student_data["name"]))
            print("-" * 20)
            print("Student Number: {}".format(self.student_number))
            print("National Code: {}".format(student_data["national_code"]))
            print("Gender: {}".format(student_data["gender"]))
            print("Marital Status: {}".format(student_data["marital_status"]))
            print("Phone Number: {}".format(student_data["phone_number"]))
            print("Mother's Name: {}".format(student_data["mothers_name"]))
            print("Father's Name: {}".format(student_data["fathers_name"]))
            print("Address: {}".format(student_data["address"]))
            print("Tuition Status: {}".format(student_data["tuition_based_or_free"]))
            print("Faculty Name: {}".format(student_data["faculty_name"]))
            print("Field of Study: {}".format(student_data["field_of_study"]))
            print("-" * 20)
        else:
            print("Student data not found.")

    def login(self):
        student_number = input("Enter your student number: ")
        national_code = input("Enter your national code: ")
        students = Student.load_student_data()

        if student_number in students and students[student_number]["national_code"] == national_code:
            # print("You have successfully logged in!")
            self.load_student(students, student_number)
            self.login_time = datetime.datetime.now()
            login_time_formatted = self.login_time.strftime("%H:%M")
            print("You have successfully logged in at:", login_time_formatted)
            self.display_menu()
        else:
            print("You have not registered yet.")
            self.register()

    def register(self):
        self.assign_money()
        student_number = input("Enter your student number: ")
        students = Student.load_student_data()
        if student_number in students:
            print("Student already exists. Please log in.")
            self.display_home_page()
        else:
            # password = input("Enter your password: ")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            name = first_name + " " + last_name
            rectangle_width = 40
            rectangle_height = 6
            print("*" * rectangle_width)
            print(f"*{'':{rectangle_width - 2}}*")
            print(f"*{name.center(rectangle_width - 2)}*")
            print(f"* {student_number.center(rectangle_width - 3)}*")
            for _ in range(rectangle_height - 4):
                print(f"*{'':{rectangle_width - 2}}*")
            print(f"*{'Please press b to continue...'.center(rectangle_width - 2)}*")
            print("*" * rectangle_width)

            user_input = input()
            if user_input.lower() == 'b':
                print('Sign up: Please select the option and enter the required information!')
                national_code = input("Enter your national code: ")
                gender = input("Enter your gender: ")
                marital_status = input("Enter your marital status: ")
                phone_number = input("Enter your phone number: ")
                mothers_name = input("Enter your mother's name: ")
                fathers_name = input("Enter your father's name: ")
                address = input("Enter your address: ")
                tuition_based_or_free = input("Enter your tuition status (based or free): ")
                faculty_name = input("Enter your faculty name: ")
                field_of_study = input("Enter your field of study: ")

                students[student_number] = {
                    # "password": password,
                    "student_number": student_number,
                    "name": f"{first_name} {last_name}",
                    "national_code": national_code,
                    "gender": gender,
                    "marital_status": marital_status,
                    "phone_number": phone_number,
                    "mothers_name": mothers_name,
                    "fathers_name": fathers_name,
                    "address": address,
                    "tuition_based_or_free": tuition_based_or_free,
                    "faculty_name": faculty_name,
                    "field_of_study": field_of_study,
                }
                Student.save_student_data(students)

                print("Registration successful!")
                self.load_student(students, student_number)
                self.display_menu()


    def display_menu(self):
        print("\nWelcome, {} {}!".format(self.first_name, self.last_name))
        while True:
            print("1. selection")
            print("2. add remove")
            print("3. Confirmation")
            print("4. Financial")
            print("5. Quit request")
            print("6. About us")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.selection()
            elif choice == 2:
                self.add_remove()
            elif choice == 3:
                self.confirmation()
            elif choice == 4:
                self.financial()
            elif choice == 5:
                self.quit_request()
            elif choice == 6:
                self.about_us()
            elif choice == 7:
                self.exit()
                exit()
            else:
                print("Invalid choice. Please try again.")

    def selection(self):
        course_data = Student.load_course_data()
        print("1. View available courses")
        print("2. Select courses")
        print("3. Go back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available Courses:")
            for course_id, course_name in course_data.items():
                print(f"{course_id}: {course_name}")
            print()

        elif choice == "2":
            course_id = input("Enter the course code to add: ")
            if course_id in course_data:
                course_name = course_data[course_id]["course_name"]
                prof_name = course_data[course_id]["professor_name"]
                students = Student.load_student_data()
                if self.student_number in students:
                    student_data = students[self.student_number]
                    student_data.setdefault("courses", {}).setdefault(course_id, {}).update(
                        {"course_name": course_name, "prof_name": prof_name}
                    )
                    Student.save_student_data(students)
                    print(f"{course_name} has been added to your course list.")
                    # self.display_course_data()
                    print()
                else:
                    print("Invalid student number.")
                print()
        elif choice == "3":
            self.display_menu()
        else:
            print("Invalid choice. Please try again.")
            print()
        self.selection()

    def add_remove(self):
        students = Student.load_student_data()

        print("1. Add a course")
        print("2. Remove a course")
        print("3. Go back")

        choice = input("Enter your choice: ")

        if choice == "1":
            course_id = input("Enter the course code to add: ")
            course_data = Student.load_course_data()

            if course_id in course_data:
                course_name = course_data[course_id]["course_name"]
                prof_name = course_data[course_id]["professor_name"]

                if self.student_number in students:
                    student_data = students[self.student_number]

                    # Check if the course is already added
                    if "courses" in student_data and course_id in student_data["courses"]:
                        print("This course is already added.")
                    else:
                        # Add the course to the student's courses
                        student_data.setdefault("courses", {}).setdefault(course_id, {}).update(
                            {"course_name": course_name, "prof_name": prof_name}
                        )
                        Student.save_student_data(students)
                        print(f"{course_name} has been added to your course list.")
                else:
                    print("Invalid student number.")
            else:
                print("Invalid course code.")

        elif choice == "2":
            if self.student_number in students:
                student_data = students[self.student_number]

                # Check if the student has any courses
                if "courses" in student_data and len(student_data["courses"]) > 0:
                    print("Your enrolled courses:")
                    for course_id, course_info in student_data["courses"].items():
                        print(f"Course ID: {course_id}")
                        print(f"Course Name: {course_info['course_name']}")
                        print(f"Professor Name: {course_info['prof_name']}")
                        print()

                    course_id = input("Enter the course code to remove: ")

                    # Check if the course exists
                    if course_id in student_data["courses"]:
                        course_name = student_data["courses"][course_id]["course_name"]
                        del student_data["courses"][course_id]
                        Student.save_student_data(students)
                        print(f"{course_name} has been removed from your course list.")
                    else:
                        print("Invalid course code.")
                else:
                    print("No courses found for this student.")
            else:
                print("Invalid student number.")

        elif choice == "3":
            self.display_menu()

        else:
            print("Invalid choice. Please try again.")

        print()
        self.add_remove()

    def confirmation(self):
        self.display_course_data()

    def financial(self):
        # self.assign_money()

        students = Student.load_student_data()
        if self.student_number in students:
            student_data = students[self.student_number]

            while True:
                print("1. View budget")
                print("2. Pay")
                print("3. Withdraw")
                print("4. Go back")

                choice = input("Enter your choice: ")

                if choice == "1":
                    budget = student_data.get("financial_id", {}).get("budget", 0)
                    print("Your current budget is:", "$", budget)

                elif choice == "2":
                    amount = float(input("Enter the amount to pay: $"))
                    budget = student_data.get("financial_id", {}).get("budget", 0)

                    if amount <= budget:
                        budget -= amount
                        student_data.setdefault("financial_id", {})["budget"] = budget
                        Student.save_student_data(students)
                        print("Payment of ${} has been successfully made.".format(amount))
                        print("Your current budget is: ${}".format(budget))
                    else:
                        print("Insufficient budget to make the payment.")

                elif choice == "3":

                    amount = float(input("Enter the amount to withdraw: $"))
                    budget = student_data.get("financial_id", {}).get("budget", 0)

                    budget += amount
                    student_data.setdefault("financial_id", {})["budget"] = budget
                    Student.save_student_data(students)
                    print("Withdrawal of ${} has been successful.".format(amount))
                    print("Your current budget is: ${}".format(budget))

                elif choice == "4":
                    self.display_menu()

                else:
                    print("Invalid choice. Please try again.")

                Student.save_student_data(students)
        else:
            print("Student data not found.")

        self.display_menu()

    def quit_request(self):
        reason = input("Enter the reason for dropping out: ")
        students = Student.load_student_data()

        if self.student_number in students:
            student_data = students[self.student_number]
            student_data["status"] = "Dropped Out"  # Add the "status" key
            student_data["reason"] = reason  # Add the "reason" key
            Student.save_student_data(students)
            print("Your request for dropping out has been submitted.")
            print("\nStudent Number: {}".format(self.student_number))
            print("Status: Dropped Out")
            print("Reason: {}".format(reason))
        else:
            print("Invalid student number.")
        self.display_menu()

    def about_us(self):
        students = Student.load_student_data()
        student_data = students[self.student_number]
        if "status" in student_data and student_data["status"] == "Dropped Out":
            print("Status: Dropped Out")
            print("Reason: {}".format(student_data["reason"]))
            print("Base dige khaste shodm!")
        else:
            self.display_student_info()
            self.display_course_data()

    def exit(self):
        self.logout_time = datetime.datetime.now()
        login_time_formatted = self.login_time.strftime("%H:%M")
        print("logged out at ", login_time_formatted)
        print("Goodbye!")
