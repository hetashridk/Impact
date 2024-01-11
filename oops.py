class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunct(self):
        print("Hello my name is " + self.name)
        print(self.age)
p1 = Person("Python", 3)
p1.myFunct()


class Person:
    def __init__(h, name, age):
        h.name = name
        h.age = age
    def myFunct(h):
        print("Hello my name is " + h.name)
        print(h.age)
p1 = Person("Python", 3)
p1.myFunct()

# self parameter is a reference to the cureent instance of class and is used to access variables that belongs to the class
# it doesn't have have to named self, you can csll whatever you like, but has to be the first parameter of any function in class

