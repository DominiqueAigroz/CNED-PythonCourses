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

### list
C'est une séquence d'éléments  

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


