### Student now has all attributes & methods of the Person class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    pass


luke = Student("Luke", 24)

print(luke.name, luke.age)
