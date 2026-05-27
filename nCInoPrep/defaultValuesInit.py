class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    
p1 = Person("Ryan")
p2 = Person("Luke", 24)


print(p1.age)
print(p2.age)