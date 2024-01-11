# method overriding => runtime 

class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swin(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("penguine can't fly")
    
    def swin(self):
        print("penguine can swim")

# common interface
def flying_Bird(bird):
    bird.fly()

blu = Parrot()
peggy = Penguin()

flying_Bird(blu)
flying_Bird(peggy)