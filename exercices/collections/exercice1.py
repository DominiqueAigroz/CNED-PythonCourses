# 1. Créer une collection de nombre entier 2, 5, 22, 35, 73, 104
numbers = list((2, 5, 22, 35, 73, 104))

# 2. Afficher chaque élément de la collection
print('Les nombres de la collection:')
for n in numbers:
    print(n)

# 3. Afficher uniquement les nombres paires
print('Les nombres paires de la collection:')
for n in numbers:
    if n % 2 == 0:
        print(n)

# 4. Créer une nouvelle collection en ajoutant 100 à chaque élément de la collection
numbers100 = list()
for n in numbers:
    numbers100.append( n + 100 )
print('Les nombres de la collection ajoutant 100:')
print(numbers100)

# 5. Créer une nouvelle collection en triant les élément du plus grand au plus petit
numbersOrdered = sorted(numbers, key=None, reverse=True)
print('Les nombres de la collection trié de manière descendante:')
print(numbersOrdered)