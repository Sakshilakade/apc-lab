class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")

    def display(self):
        print("Name:", self.name)

    def __del__(self):
        print("Destructor called")


s = Student("Sakshi")
s.display()

del s