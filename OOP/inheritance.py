class Animal: 
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def make_sound(self, sound):
        print(f"The {self.name} y now making a sound: ", sound)
        
    def eat_something(self):
        print(f"Now {self.name} is eating")

class Dog(Animal):
    def run(self):
        print(f"Now {self.name} is running")
        
class Cat(Animal):
    def jump(self):
        print(f"Now {self.name} is jumping")
        
dog1 = Dog("Chase", 4, "Brown")
cat1 = Cat("Terry", 2, "White")

dog1.make_sound("bark")
cat1.make_sound("meow")

