# functions

# One function without parameter
def displayHello():
    print("Hello")

# One function with one parameter
def displayHelloW(s):
    print("Hello " + s)

# One function with two parameters and returning the sum
def sumNumber(n1,n2):
    return n1 + n2

# One function with three parameters and returning 
# the sum of n1 and n2 and multiply by m1
def sumNumberMultiply(n1,n2,m1):
    n = n1 + n2
    sm = n * m1
    return sm

# Call the displayHello function
displayHello()

# Call the displayHelloW function with s1 as parameter
s1 = 'World'
displayHelloW(s1)

# Call the sumNumber function with 3 and 5 as parameters
# Assign its returned value to n var.
n = sumNumber(3,5)
print(n)

n = sumNumberMultiply(3,5,10)
print(n)
