# Sequences
Vous trouverez toutes les séquences du cours au sein du dossier /sequences

## Built-in Types
Ce sont les types de base du langage Python.
https://docs.python.org/3/library/stdtypes.html

Les types de données de base disponible en Python
- integer (valeur entière)
- bool (valeur boolean True/False)
- decimal (valeur numérique avec virgule flottante)
- char (un caractère)
- string (une chaîne de caractères)

```python
# une variable entière
i = 0
# une chaîne de caractères
s = "hello i'm s"
# un caractère
c = 'a'
# une variable décimale
f = 10.2
# un boolean
b = True
```
![Built-in Types](/images/sequences/builtintypes/builtintype1.png)

Les variables déclarées au sein de l'application sont stockées en mémoire vive.  
L'adressage mémoire est lié au processeur et au système d'exploitation.  
Sur un processeur 32bit, les adresses mémoire seront sur 32bits.  
Sur un processeur 64bit, elles seront sur 64bits.  

![Memory](/images/sequences/builtintypes/memory1.png)


## Operators

Il existe, comme dans tous les langages de programmation des opérateurs :  
<code>
\+ - / * %  
\=  
\==  
\!=  
</code>

![Operators](/images/sequences/builtintypes/operators.png)

```python
# assignation
numb1 = 10
# add 100 to numb1
numb2 = numb1 + 100
# is equal
bEq = numb1 == numb2
# is different
bNEq = numb1 != numb2
```

Les opérateurs de comparaison : 

https://docs.python.org/3/library/stdtypes.html#comparisons

| Opérateur | Signification |
| --------- | ------------- |
| < | plus petit que |
| <= | plus petit que ou égal |
| > | plus grand que |
| >= | plus grand que ou égal |
| == | égal |
| != | pas égal |

## Array

Les tableaux permettent de stocker plusieurs éléments de types:  integer, string, char, objet, ...  
Les tableaux sont indéxés de 0 à n

```python
# an array of string
words = ['hello', 'world', '!!!!']
# access the first element of the array
s = words[0]
print(s)
# output
# hello
```

![Operators](/images/sequences/array/array.png)


## Collections

Les collections ne sont pas des tableaux, même si elles permettent de stocker des données.  
Les éléments des tableaux sont indexés de 0..n alors que les collections gèrent les éléments avec un algorithme interne.  
Les collections sont du type **[iterable]**, ce qui signifie qu'on peut parcourir ses éléments

[Voir documentation Phyton](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)  

[Voir code en exemple](/sequences/collections/cols.py)


### list
C'est une séquence d'éléments  
[Voir documentation Phyton](https://docs.python.org/3/library/stdtypes.html#lists)

```python
# an empty list
lst1 = list([])
# a list with 3 caracters
lst2 = list('abc')
# returns ['a', 'b', 'c']

# a list with 3 numbers
lst3 = list((1,2,3))
# returns [1, 2, 3]
```

### dict

[Voir documentation Phyton](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

Contient des éléments identifiés par une clé et contenant une valeur  
L'exemple ci-après :  
'one' c'est la clé  
1 c'est la valeur

```python
# create a dictionary with three items:
# 'one' -> 1
# 'two' -> 2
# 'three' -> 3
dicta = {'one': 1, 'two': 2, 'three': 3}

# run through 
# iterate keys in collection
for k in dicta:
    print(k)

# iterate keys and values in collection
for k, v in dicta.items():
    print('Key='+k+' value='+str(v))

# iterate values in collection
for v in dicta.values():
    print('Value='+str(v))

# iterate keys in collection
for k in dicta.keys():
    print('Keys='+k)
```

### tuple

La collection tuple est une collection immutable.  
Cela signifie que c'est une collection dont les éléments ne peuvent être modifiés.  
[Voir documentation Phyton](https://docs.python.org/3/library/stdtypes.html#tuples)

```python
# create a tuple collection with 1, 2, 3 and 4 numbers
t1 = tuple((1,2,3,4))
print(t1)
# try to assign a new value to first item
t1[0] = 10 # ERROR at runtime !!!!!
print(t1)
```

### string

string est le type qui représente une chaîne de caractères  
[Voir documentation Phyton](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

[Voir code en exemple](/sequences/collections/str.py)
```python
# assignation
s = "hello world"
print(s)
# output
# hello world

# capitilize the first letter of the string
cap = s.capitalize()
print(cap)
# output
# Hello world

# Upper case all letters
up = s.upper()
print(up)
# output
# HELLO WORLD

# Lower case all letters
s = "hElLo WoRlD"
lo = s.upper()
print(up)
# output
# hello world
```

Remplacement d'une chaîne par une autre
```python
s = "hello world"
s1 = s.replace("world", "dude")
print(s1)
# output
# hello dude
```

Rechercher une chaîne au sein d'une chaîne de caractères
```python
idx = s1.rfind("du")
print(idx)
# output
# 6

idx = s1.rfind("wor")
print(idx)
# output
# -1 not found
```

Conversion d'une chaîne en nombre
```python
nb = "1200"
isnumber = nb.isdigit()
print(isnumber)
# output
# True 

nbf = "120a0"
isnumber = nbf.isdigit()
print(isnumber)
# output
# False 
```


## Fonctions

Les fonctions permettent d'encapsuler des traitements.  
Une fonctions est identifiée par son noms, ses paramètres et sa valeur de retour.  
[Voir documentation Phyton](https://docs.python.org/3/library/stdtypes.html#functions)

[Voir code en exemple](/sequences/functions/fnc.py)

On définit une fonction avec le mot clé **def**  
La fonction se termine par **:**  

L'exemple ci-après définit une fonction dont le nom est displayHello  
qui n'a pas de paramètre et ne retourne aucune valeur.
```python
# One function without parameter
def displayHello():
    print("Hello")
```

On appelle la fonction en spécifiant son nom.
```python
# Call the displayHello function
displayHello()
```


L'exemple ci-après définit la fonction displayHelloW  
avec un paramètre dont le nom est **s**.
```python
# One function with one parameter
def displayHelloW(s):
    print("Hello " + s)
```

On appelle la fonction en spécifiant son nom et le paramètre qu'il prend en entrée.
```python
# Call the displayHelloW function with s1 as parameter
s1 = 'World'
displayHelloW(s1)
```

L'exemple ci-après définit la fonction sumNumber  
qui prend deux paramètres en entrée **n1** et **n2**.  
La fonction retourne l'addition des nombres **n1** et **n2**

```python
# One function with two parameters and returning the sum
def sumNumber(n1,n2):
    return n1 + n2
```

On appelle la fonction en spécifiant son nom et les deux paramètres qu'il prend en entrée.  
On assigne le résultat à la variable **n**.
```python
# Call the sumNumber function with 3 and 5 as parameters
# Assign its returned value to n var.
n = sumNumber(3,5)
```
