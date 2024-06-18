class students:
    def __init__(self,name,rollno,grade):
        self.name=name
        self.rollno=rollno
        self.grade=grade
    def display_info(self):
        print("NAME: ",self.name)
        print("ROLLNO: ",self.rollno)
        print("GRADE: ",self.grade)
class teachers():
    def __init__(self,name,empid,subtau):
        self.name=name
        self.empid=empid
        self.subtau=subtau
    def display_info(self):
        print("NAME: ",self.name)
        print("EMPLOYEE ID: ",self.empid)
        print("SUBJECTS TAUGHT: ",self.subtau)
class course:
    def __init__(self,code,subject,tc):
        self.code=code
        self.subject=subject
        self.tc=tc
student1=students("Aadhira",241001,1)
student2=students("Nilan",240001,1)
teacher1=teachers("Collin",123,"Maths")
teacher2=teachers("Rooby",124,"Science")
course1=course("m003","MATHS",teacher1)
course2=course("s004","SCIENCE",teacher2)
student1.display_info()
student2.display_info()
teacher1.display_info()
teacher2.display_info()
print("CODE: ",course1.code)
print("subject: ",course1.subject)
print("TEACHER ASSIGNED: ",course1.tc.name)
print("CODE: ",course2.code)
print("SUBJECT: ",course2.subject)
print("TEACHER ASSIGNED: ",course2.tc.name)
