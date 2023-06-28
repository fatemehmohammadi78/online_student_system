import pickle
import os.path
from copy import deepcopy


class Course:

    def __init__(self):
        self.file_path = 'courses.pickle'
        self.data = {
            'available_courses': {
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
            },
        }

    def course_file_exists(self) -> bool:
        return os.path.isfile(self.file_path)

    @property
    def available_courses(self) -> dict:
        self.load_data()
        return self.data['available_courses']

    def save_data(self) -> None:
        with open(self.file_path, "wb") as file:
            pickle.dump(self.data, file)

        print(f"Courses data has been saved to '{self.file_path}' file.")

    def load_data(self) -> dict:
        with open(self.file_path, "rb") as f:
            data = pickle.load(f)
        self.data = data
        return data
