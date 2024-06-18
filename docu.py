class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"
def animal_sound(animal):
    return animal.speak()
dog = Dog()
cat = Cat()
duck = Duck()
print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(duck))
