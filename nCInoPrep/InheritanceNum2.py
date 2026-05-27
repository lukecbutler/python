class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def greet(self):
        print(f"Hi, my name is, {self.fname} {self.lname}")
    

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


luke = Student("Luke", "Butler")
luke.greet()