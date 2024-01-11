# options=> inventory => 1
# inventory is stock => item no, name, quantity

# searchbyId => 101 eg =>print rice => 500kg, 50 inr  else print not available
# searchbyname => 101 eg => id => 500kg, 50 inr else print not available

# by from vendor =>check item id, name, quantity, net price

# sale the item for customer=> ask quantity 

# stop


# item = {{id: 1, name: "rice", price: 250, quantity: 5},
#         {id: 2, name: "wheat", price: 500, quantity: 7},
#         {id: 3, name: "dal", price: 750, quantity: 9}}

# print("Enter the id")
# search = int(input())

# if search == 1:
#     print("Item id: ", item[id])
#     print("Item name: ", item[name])
#     print("Item price: ", item[price])
#     print("Item quantity: ", item[quantity])
#     # print("Item id: ", item.keys())
# else:
#     print("Not Available")

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

id1= [101, 102, 103]
name=["rice", "dal", "wheat"]
price = [50, 500, 750]
quantity = [5, 5, 5]
item = {1:id1,
        2:name,
        3: price,
        4: quantity}


while True:
    print("Enter your choice")
    choice = int(input())
    if choice == 1:
        print(item)
    
    elif choice == 2:
        id2 = int(input())
        p=id1.index(id2)
        print(name[p])
        print(quantity[p])
        print(price[p])
        
    elif choice == 3:
        name1 = input()
        p=name.index(name1)
        print(id1[p])
        print(quantity[p])
        print(price[p])
        

    elif choice == 4:
        id2 = int(input())
        id1.append(id2)
        name1 = input()
        name.append(name1)
        price1 = int(input())
        price.append(price1)
        quantity1 = int(input())
        quantity.append(quantity1)

    elif choice == 5:
        print("The quantity for all the thing is 5 only")
        id2 = int(input())
        quantity1 = int(input())
        if quantity1 > 5:
            print("This quantity isn't available")
        else:
            quantity[id2] = quantity[id2] - quantity

    elif choice == 6:
        exit(1)

    else:
        print("Invalid choice")
        


