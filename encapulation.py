class Computer:
    def __init__(self):
        self.__maxprice = 900   #__maxprice is a private variable
         #_maxprice will be protected variable
    
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# changing price
c.__maxprice = 1000
c.sell()

# using setter
c.setMaxPrice(1000)
c.sell()