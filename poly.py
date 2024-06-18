class animal():
    def sound(self):
        print("animals make sound")
class dog(animal):
    def sound(self):
        print("dogs bark")
class bird(animal):
    def sound(self):
        print("birds sing")
d1=dog()
d1.sound()
b1=bird()
b1.sound()
