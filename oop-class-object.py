class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course: 
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.student = []
    def add_student(self, student):
        if len(self.student) < self.max_student:
            self.student.append(student)
            return True
        return False
    def get_average(self):
    	sum = 0
    	for value in course.student:
    		sum += value.get_grade()
    	return sum / len(self.student)  
s1 = Student("Ashish", 21, 100)
s2 = Student("Ankit", 26 , 90)
s3 = Student("Amit",21 ,22)
course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.student)
print(course.get_average())
