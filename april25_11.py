class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        print("NAME: ",self.name)
        print("AGE: ",self.age)
        print("GRADE: ",self.grade)
    def promote(self):
        self.grade+=1
student1=student("Aadhira",2,1)
student1.display_info()
student1.promote()
print("AFTER PROMOTION")
student1.display_info()

    
        
