import pickle

courses = {
    "CSE101": {
        "course_name": "Introduction to Computer Science",
        "professor_name": "Dr. Hajipour"
    },
    "MTH202": {
        "course_name": "Linear Algebra",
        "professor_name": "Prof. Isazadeh"
    },
    "PHY301": {
        "course_name": "Quantum Physics",
        "professor_name": "Dr. Lotfi"
    }
}

# Save the courses dictionary to a pickle file
with open("courses.pickle", "wb") as file:
    pickle.dump(courses, file)

# print("Courses have been saved to 'courses.pickle' file.")


def read_courses_from_pickle(courses):
    with open(courses, "rb") as file:
        courses = pickle.load(file)
    return courses
