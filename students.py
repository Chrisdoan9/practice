class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
class Course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
s1 = student('Tim',19,95)
s2 = student('Bill',19,85)
s3 = student('Jill',19, 75)
course = Course('Science',2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)