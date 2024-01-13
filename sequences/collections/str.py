# string
s = "hello world"
print(s)
s1 = s.replace("world", "dude")
print(s1)
idx = s1.rfind("du")
print(idx)
idx = s1.rfind("wor")
print(idx)

# Upper case the first letter
cap = s.capitalize()
print(cap)
# Upper case all letters
up = s.upper()
print(up)
n = 1200
nb = "1200"
isnumber = nb.isdigit()
print(isnumber)
nbf = "120a0"
isnumber = nbf.isdigit()
print(isnumber)
# Convert a string to an integer
n1 = int(nb)
print(n1)
# Convert a string to a float
nb = "1200.95"
# Exception cannot convert . char to integer
# n2 = int(nb) 
# print(n2)
n2 = float(nb)
print(n2)
# Convert a string to an float
nb = "1400"
n3 = float(nb)
print(n3)

# split
s = "hello;world;toto;by"
sp = s.split(';')
print(sp)

# formatting
s = "My number integer is {0}, my float is {1}".format(n1, n2)
print(s)
s = "My number integer is %d, my float is %f" % (n1, n2)
print(s)
s = "My number integer is %d, my float is %.1f" % (n1, n2)
print(s)
s = "My number integer is %d, my float is %d" % (n1, n2)
print(s)
# n1 display in hexadecimal
s = "My number integer in hexa is %x" % (n1)
print(s)