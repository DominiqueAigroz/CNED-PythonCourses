# Objects in Python

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
    # Gets the rectangle's width
    def getWidth(self):
        return self._width
    # Sets the rectangle's width
    def setWidth(self, w):
        self._width = w
    # Gets the rectangle's height
    def getHeight(self):
        return self._height
    # Sets the rectangle's height
    def setHeight(self, w):
        self._height = w
    # Gets the rectangle's top position
    def getTop(self):
        return self._top
    # Sets the rectangle's top position
    def setTop(self, w):
        self._top = w
    # Gets the rectangle's left position
    def getLeft(self):
        return self._left
    # Sets the rectangle's left position
    def setLeft(self, w):
        self._left = w

    # Gets the rectangles' perimeter
    def getPerimeter(self):
        return (2 * self._height) + (2 * self._width)
    # Gets the rectangles' square
    def getSquare(self):
        return self._height * self._width
    
    # Display the rectangle to console
    def ToConsole(self):
        s = "Rectangle: Width {0}, Height {1}, Top {2}, Left {3}".format(self._width, self._height, self._top, self._left)
        print(s)

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

    # Gets the rectangle's radius
    def getRadius(self):
        return self.__radius
    # Sets the rectangle's radius
    def setRadius(self, r):
        self.__radius = r
    # Display the round rectangle to console
    def ToConsole(self):
        s = "Round Rectangle: Width {0}, Height {1}, Top {2}, Left {3}, radius {4}".format(self._width, self._height, self._top, self._left, self.__radius)
        print(s)


# Create a new object r1 Rectangle (Rect)
r1 = Rect()
# Assigns its width
r1.setWidth(100)
# Assigns its height
r1.setHeight(50)
# Assigns its top position
r1.setTop(500)
# Assigns its left position
r1.setLeft(300)
r1.ToConsole()
# Create another Rectangle object r2
r2 = Rect(10,20,500,800)
r2.ToConsole()

p1 = r1.getPerimeter()
print(p1)
a1 = r1.getSquare()
print(a1)
# Create a new object rd1 round rectangle (RoundRect)
rd1 = RoundRect(100,200,5000,8000,7)
rd1.ToConsole()
