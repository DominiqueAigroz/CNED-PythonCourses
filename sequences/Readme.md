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


## Classes

Les classes sont qualifiés également d'objets  
Comme dans les langages Orienté Objets tels que Java, C++, C#, ... le mot clé **class** permet de définir un objet.  

[Voir documentation Phyton](https://docs.python.org/3/tutorial/classes.html)

[Voir code en exemple](/sequences/classes/object.py)

Les classes possèdent des variables membres qui permettent de conserver l'état de l'objet créé.  
Les classes possèdent également des méthodes (fonctions) qui permettent d'intéragir avec l'objet.  

Les variables membres ont trois niveaux d'accessibilité :  
- publique
- protégé
- privée

En notation UML on utilise la notation :  
\+ pour publique  (public)  
\# pour protégé  (protected)  
\- pour privé  (private)  


Prenons l'exemple d'une classe rectangle

![Classe rectangle](/images/sequences/classes/Rect-Object-Python.png)


Définition de notre classe rectangle  
```python
# Class managing a rectangle
class Rect:
```
  
Ajout des variables membres qui caractérise notre rectangle  
Ici, en mode d'accéssibilité publique  

```python
# Class managing a rectangle
class Rect:
    # public members 
    width = 0
    height = 0
    top = 0
    left = 0
```


Ajout de deux méthodes qui permettent de manipuler la largeur de notre rectangle  
Attention, il faut passer **self** comme premier paramètre afin d'accéder à notre objet  

```python
# Class managing a rectangle
class Rect:
    # Gets the rectangle's width
    def getWidth(self):
        return self._width
    # Sets the rectangle's width
    def setWidth(self, w):
        self._width = w
```

Création d'un nouvel objet de type Rect  

```python
# Create a new object r1 Rectangle (Rect)
r1 = Rect()
# Assigns its width
r1.setWidth(100)
n = r1.getWidth()
print(n)
# output
# 200
```

Comme on peut le voir, le premier paramètre **self** n'est passé en paramètre.  
C'est lui qui l'assigne en interne.  

Il existe une méthode que l'on appelle constructeur, qui est automatiquement appelé lors de la création d'un nouvel objet.  
On appelle cela, instantiation d'un objet. C'est la création d'un nouvel objet à partir de notre **class**.  
Le constructeur **__init__** en Python.  

```python
# Class managing a rectangle
class Rect:
    # Ctor
    def __init__(self) -> None:
        self.width = 0
        self.height = 0
        self.top = 0
        self.left = 0
```

Maintenant on peut définir nos variables membres comme étant privée afin d'empêcher l'accès direct.  
En Python on utilise le _ :  
aucun **_** pour publique  (public)  
\_ un seul **_** pour protégé  (protected)  
\__ deux **_** pour privé  (private)  

Notre classe avec les variables membres en privée  
```python
# Class managing a rectangle
class Rect:
    # private members 
    __width = 0
    __height = 0
    __top = 0
    __left = 0
```

On peut spécifier des paramètres à notre constructeur afin d'initialiser nos variables membres à la création de l'objet.  

```python
# Class managing a rectangle
class Rect:
    # private members (double underscore)
    __width = 0
    __height = 0
    __top = 0
    __left = 0
    # Ctor
    def __init__(self, InTop, InLeft, InWidth, InHeight) -> None:
        self.__width = InWidth
        self.__height = InHeight
        self.__top = InTop
        self.__left = InLeft
```

On ne pourra plus créer un nouvel objet de type Rect sans spécifier les paramètres  

```python
# Create a new object r1 Rectangle (Rect)
r1 = Rect() # ERR

# Create a new object r1 Rectangle (Rect)
r1 = Rect(10,20,100,200) # Valide
```

Si on veut pouvoir créer notre objet avec ou sans paramètre, alors on utiliser la notation des paramètres par défaut.  

```python
# Class managing a rectangle
class Rect:
    # private members (double underscore)
    __width = 0
    __height = 0
    __top = 0
    __left = 0
    # Ctor
    def __init__(self, InTop=0, InLeft=0, InWidth=0, InHeight=0) -> None:
        self.__width = InWidth
        self.__height = InHeight
        self.__top = InTop
        self.__left = InLeft
```

Maintenant on peut créer un nouvel objet de type Rect sans spécifier les paramètres  

```python
# Create a new object r1 Rectangle (Rect)
r1 = Rect() # equivalent Rect(0,0,0,0)

# Create a new object r2 Rectangle (Rect)
r2 = Rect(10,20,100,200) 

# Create a new object r2 Rectangle (Rect)
r3 = Rect(10,20) # equivalent Rect(10,20,0,0)
```

### Héritage
On peut hériter d'une classe existante afin d'ajouter des fonctionnalités.  
Prenons l'exemple d'un rectangle arrondi qui dérive de notre classe rectangle.  
Finalement, notre rectangle arrondi implémente un rectangle et ajoute la fonctionnalité d'avoir des coins arrondis matéralisés par un radius.  

![Classe rectangle arrondi](/images/sequences/classes/RoundRect-Object-Python.png)


```python
# Class managing a rounded rectangle deriving from our rectangle
class RoundRect(Rect):
    # private members (double underscore)
    __radius = 0
```

Les variables membres de notre classe Rect sont du type privée et ne peuvent accédées par notre classe RoundRect.  
Afin qu'on puisse les accéder, on va changer le type d'accès aux variables membres de Rect et les mettre en protected.  


```python
# Class managing a rectangle
class Rect:
    # protected members (single underscore)
    _width = 0
    _height = 0
    _top = 0
    _left = 0
    # Ctor
    def __init__(self, InTop=0, InLeft=0, InWidth=0, InHeight=0) -> None:
        self._width = InWidth
        self._height = InHeight
        self._top = InTop
        self._left = InLeft
```

Ainsi on pourra les accéder depuis notre classe RoundRect.  


```python
# Class managing a rounded rectangle deriving from our rectangle
class RoundRect(Rect):
    # private members (double underscore)
    __radius = 0

    # Ctor
    def __init__(self, InTop=0, InLeft=0, InWidth=0, InHeight=0, InRadius=0) -> None:
        self._width = InWidth
        self._height = InHeight
        self._top = InTop
        self._left = InLeft
        self.__radius = InRadius
```

Le radius peut rester private car pour l'instant on n'a pas prévu de pouvoir dériver de RoundRect.  