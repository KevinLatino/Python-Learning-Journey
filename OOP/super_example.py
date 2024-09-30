class LivingBeing:
    def __init__(self, name):
        self.name = name 
        
    def greeting(self):
        print(f"{self.name} is saying hi")

class Person(LivingBeing):
    def  __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def greeting(self):
        super().greeting()
        print("My age is", self.age)
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def greeting(self):
        super().greeting()
        print(f"My student ID is {self.student_id}")

student1 = Student("Kevin", 18, 201998)
student1.greeting()