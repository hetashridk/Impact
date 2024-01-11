# dict to list
d = {"abc": 20, "xyz": 30, "hdk": 40, "com": 50}
l1 = list(d)
print(l1)

# list to dic
d1 = dict([[1, 2],[3, 4]])
print(d1)

# int to float => implicit conversion
num1 = 12
num2 = 12.4
sum = num1 + num2
print(type(num1))
print(type(num2))
print(type(sum))

# explicit conversion
str1 = int("8")
strsum = num1 + str1
print(type(strsum))
print(type(str1))
