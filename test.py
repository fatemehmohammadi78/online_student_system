student_number = input("Enter student number: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name = first_name+" "+last_name
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
