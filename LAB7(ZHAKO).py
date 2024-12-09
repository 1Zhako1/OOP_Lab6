import pickle


class CourseGrade:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []   # stu_ID = []
        self.grades = []  # grades = []

    def __str__(self):
        return f"{self.course_name}: IDs {self.stu_ID}, Grades {self.grades}"

    def get_details(self):
        self.course_name = input("Enter the name of the course: ")
        for i in range(0, 5):
            self.stu_ID.append(input("Enter Student's ID: "))
        for i in range(0, 5):
            self.grades.append(int(input("Enter Student's Grade (0-100): ")))

    def display(self):
        print("Name of the course:", self.course_name)
        print("Student ID:", self.stu_ID)
        print("Student's grades:", self.grades)


def main():
    file_name = "grades_info.dat"
    courses = []


    for i in range(4):
        print(f"Enter details for Course {i + 1}:")
        course = CourseGrade()
        course.get_details()
        courses.append(course)


    with open(file_name, "ab") as f:
        for course in courses:
            pickle.dump(course, f)
    print("\nCourses saved to file!")


    print("\nReading courses from the file...")
    try:
        with open(file_name, "rb") as f:
            while True:
                try:
                    course = pickle.load(f)
                    course.display()
                except EOFError:
                    break
                except Exception as e:
                    print(f"An error occurred while reading the file: {e}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        main()

    def main():
        file_name = "grades_info.dat"
        while True:
            print("\nMenu:")
            print("1. Create and Save 4 Courses")
            print("2. Read and Display Courses from File")
            print("3. Exit")
            option = input("Enter your choice (1-3): ")

            if option == "1":
                courses = create_courses()
                save_courses_to_file(courses, file_name)
            elif option == "2":
                courses = read_courses_from_file(file_name)
                display_courses(courses)
            elif option == "3":
                print("Exiting the program")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    if __name__ == "__main__":
        main()