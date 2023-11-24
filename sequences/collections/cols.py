# an empty list
lst1 = list([])
print(lst1)
# output
# []

# a list with 3 caracters
lst2 = list('abc')
print(lst2)
# output 
# ['a', 'b', 'c']
for c in lst2:
    print(c)

# a list with 3 numbers
lst3 = list((1,2,3))
print(lst3)
# output 
# [1, 2, 3]


# an dictionary
dicta = {'one': 1, 'two': 2, 'three': 3}
print(dicta)

dictb = dict([('two', 2), ('one', 1), ('three', 3)])
print(dictb)
# access an element of the dictionary
eltwo = dictb['two']
print(eltwo)
# modify an element's value of the dictionary
dictb['two'] = 27
eltwo = dictb['two']
print(eltwo)
# add 10 to the element
dictb['two'] = dictb['two'] + 10
print(dictb['two'])

dictb['two'] += 10
print(dictb['two'])

# iterate keys in collection
for k in dictb:
    print(k)

# iterate keys and values in collection
for k, v in dictb.items():
    print('Key='+k+' value='+str(v))

# iterate values in collection
for v in dictb.values():
    print('Value='+str(v))

# iterate keys in collection
for k in dictb.keys():
    print('Keys='+k)


# tuples
t1 = tuple((1,2,3,4))
print(t1)
t1[0] = 10
print(t1)
