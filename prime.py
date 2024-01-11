 
def isPrime(n, i):
 
    if (n == 0 or n == 1):
        return False
 
    if (n == i):
        return True
 
    if (n % i == 0):
        return False
 
    i += 1
 
    return isPrime(n, i)
 
if (isPrime(35, 2)):
    print("true")
else:
    print("false")