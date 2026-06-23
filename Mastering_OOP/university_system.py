class Student:
    def __init__(self, name, student_id, department, level):
        self.name = name
        self.student_id = student_id
        self.department = department
        self.level = level
        self.enrolled_courses = []  # a student starts with no courses

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)  # tell the course a student just joined
        print(f"{self.name} enrolled in {course.title}")

    def view_courses(self):
        for course in self.enrolled_courses:
            print(f"- {course.title} ({course.course_code})")

    def to_dict(self):
        return{
                'name': self.name,
                'id': self.student_id,
                'department': self.department,
                'level': self.level,
                'courses': [course.title for course in self.enrolled_courses]
            }

    



class Course:
    def __init__(self, title, course_code, units):
        self.title = title
        self.course_code = course_code
        self.units = units
        self.enrolled_students = []
        self.lecturer = None  # no lecturer assigned yet

    def add_student(self, student):
        self.enrolled_students.append(student)

    def assign_lecturer(self, lecturer):
        self.lecturer = lecturer
        print(f"{lecturer.name} assigned to {self.title}")

    def get_enrolled_count(self):
        return len(self.enrolled_students)
    
    def to_dict(self):
        return{
                'title': self.title,
                'code': self.course_code,
                'units': self.units,
            }



class Lecturer:
    def __init__(self, name, lecturer_id, department):
        self.name = name
        self.lecturer_id = lecturer_id
        self.department = department
        self.courses = []  # plural — can teach multiple
        self.grades = {}   # {student_id: {course_code: score}}

    def assign_to_course(self, course):
        self.courses.append(course)
        course.assign_lecturer(self)

    def assign_grade(self, student, course, score):
        if student.student_id not in self.grades:
            self.grades[student.student_id] = {}
        self.grades[student.student_id][course.course_code] = score
        print(f"{student.name} scored {score} in {course.title}")

    def view_students(self, course):
        print(f"Students in {course.title}:")
        for student in course.enrolled_students:
            print(f"  - {student.name}")

    def to_dict(self):
        return{
                'name': self.name,
                'id': self.lecturer_id,
                'department': self.department,
                'courses': [course.title for course in self.courses]
            }



class Department:
    def __init__(self, name):
        self.name = name 
        self.courses = []
        self.lecturers = []
        self.students =[]


    def receive_students(self, student):
        self.students.append(student)
    
    def list_students(self):
        for student in self.students:
            print(student.to_dict())

    def receive_lecturers(self, lecturer):
        self.lecturers.append(lecturer)
    
    def list_lecturers(self):
        for lecturer in self.lecturers:
            print (lecturer.to_dict())

    def add_courses(self, course):
        self.courses.append(course)
    
    def list_courses(self):
        for course in self.courses:
            print (course.to_dict())



student1 = Student('Toluwani', 18, 'Mechatronics', 200)
lecturer1 =  Lecturer('Mr. Adeyemi', 2, 'Mechatronics')
course1 = Course('Intro to Mechatronics', 'Mec 213', 3)
department1 = Department('Mechatronics')

department1.receive_students(student1)
department1.receive_lecturers(lecturer1)
department1.add_courses(course1)

department1.list_students()
department1.list_lecturers()
department1.list_courses()




