class Student:
    total_students = 0  

    def __init__(self, name, teacher=None):
        self.name = name
        self.teacher = teacher      
        self.courses = []           
        Student.total_students += 1

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    @staticmethod
    def get_total_students():
        return Student.total_students


class Teacher:
    total_teachers = 0

    def __init__(self, name):
        self.name = name
        self.courses = []
        Teacher.total_teachers += 1

    def create_course(self, course_name):
        course = Course(course_name, self)
        self.courses.append(course)
        return course

    @staticmethod
    def get_total_teachers():
        return Teacher.total_teachers


class Course:
    total_courses = 0

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        Course.total_courses += 1

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    @staticmethod
    def get_total_courses():
        return Course.total_courses
    
if __name__ == "__main__":

    teacher1 = Teacher("Іваненко")

    course1 = teacher1.create_course("Програмування")
    course2 = teacher1.create_course("Алгоритми")

    student1 = Student("Олег", teacher1)
    student2 = Student("Марія", teacher1)

    student1.enroll_course(course1)
    student1.enroll_course(course2)

    student2.enroll_course(course1)

    print("Кількість студентів:", Student.get_total_students())
    print("Кількість викладачів:", Teacher.get_total_teachers())
    print("Кількість курсів:", Course.get_total_courses())

    print("Студенти на курсі Програмування:")
    for s in course1.students:
        print(s.name)