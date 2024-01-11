class CompleNumber:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.image = i

    def get_data(self):
        print(f'{self.real} + {self.image}j')
    
num1 = CompleNumber(2, 3)
num1.get_data()

num2 = CompleNumber(5)
num2.attr = 10
print((num2.real, num2.image, num2.attr))
print(num1.attr)