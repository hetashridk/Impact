#mutable, we can change value, append value

a = [1, 2.2, 'python', "Het", 4, 7, 10]
print(a[2])
print(a)

#slicing
print(a[0:3])

#to print alternate element
print(a[0::2])   #2 is number of steps we have to jump

#print the reverse list
print(a[::-1])

b = 4 + 2J
print(b)

# b = i
# print(b)

# will give false as they are identical not same
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)   

l1.pop()
print(l1)

l2.remove(1)
print(l2)

l1.clear()   #in clear reference will be there
print(l1)

#in delete the refernce will delete

l2.append("Hetashri")
print(l2)

l3 = [1, 2, 3, 4, 5]
l3.reverse()
print(l3)

print(l3.index(3))
print(l3.count(4))

l4 = [12, 45, 1, 25, 100, 98]
l4.sort()
print(l4)




