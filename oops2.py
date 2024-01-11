class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("swim faster")


# child class
class Penguine(Bird):
    def __init__(self):

        print("Penguine is ready")
        # super functions:- we can access the constructor only of parent class
        super().__init__()
    def whoisThis(self):
        print("Penguine")
    def run(self):
        print("Run faster")


peggy = Penguine()
peggy.whoisThis()
peggy.swim()
peggy.run()