import random

ran = random.randint(1, 11)


print("Enter the number of your choice between 1 to 11 ")
chances = 0
while(chances < 5):
    num = int(input())
    if num > ran:
        print("The your input number is more than generated number.\nEnter another number")

    elif num < ran:
        print("The your input number is less than generated number.\n Enter another number")
    
    else:
        print("You got it")
    chances = chances + 1