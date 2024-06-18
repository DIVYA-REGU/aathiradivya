class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("Animals make sound")
class Dog(Animal):
    def speak(self):
        return "bark"
class Cat(Animal):
    def speak(self):
        print("meow")
class Bird(Animal):
    def speak(self):
        print("chirps")
dog=Dog("timmy","3")
cat=Cat("poose",2)
bird=Bird("sulu",3)
print(dog.name,"makes",dog.speak())
    
          
    
          
    
