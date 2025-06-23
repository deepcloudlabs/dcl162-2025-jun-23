import random
from abc import abstractmethod, ABC


# interface
class Shape2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def circumference(self) -> float:
        pass

#interface
# Abstract Base Class (ABC)
class Shape3D(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass


class Square(Shape2D):
    def __init__(self, side: float) -> None:
        self.__side = side

    @property
    def side(self) -> float:
        return self.__side

    def area(self) -> float:
        print("Square.area() called.")
        return self.__side * self.__side

    def circumference(self) -> float:
        print("Square.circumference() called.")
        return 4 * self.__side

    def __str__(self) -> str:
        return f"Square(side={self.__side})"


class Circle(Shape2D):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def area(self) -> float:
        print("Circle.area() called.")
        return 3.141592653589793 * self.__radius * self.__radius

    def circumference(self) -> float:
        print("Circle.circumference() called.")
        return 2 * 3.141592653589793 * self.__radius

    def __str__(self) -> str:
        return f"Circle(radius={self.__radius})"


class Triangle(Shape2D):
    def __init__(self, base: float, height: float) -> None:
        self.__base = base
        self.__height = height

    @property
    def base(self) -> float:
        return self.__base

    @property
    def height(self) -> float:
        return self.__height

    def area(self) -> float:
        print("Triangle.area() called.")
        return self.__base * self.__height / 2.0

    def circumference(self) -> float:
        print("Triangle.circumference() called.")
        return self.__base * 2 + self.__height * 2

    def __str__(self) -> str:
        return f"Triangle(base={self.__base}, height={self.__height})"


class Cube(Shape2D, Shape3D):
    def __init__(self, side: float) -> None:
        self.__side = side

    def volume(self) -> float:
        print("Cube.volume() called.")
        return self.__side * self.__side * self.__side

    def area(self) -> float:
        return 6 * self.__side * self.__side

    def circumference(self) -> float:
        return 12 * self.__side

    def __str__(self) -> str:
        return f"Cube(side={self.__side})"


class Sphere(Shape3D):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def volume(self) -> float:
        print("Sphere.volume() called.")
        return 4.0 / 3.0 * 3.141592653589793 * self.__radius * self.__radius * self.__radius

    def __str__(self) -> str:
        return f"Sphere(radius={self.__radius})"


shape1: Shape2D = Square(10)
shape2: Shape2D = Triangle(10, 5)
shape3: Shape3D = Cube(10)
print(shape1.area())
print(shape1.circumference())
print(shape2.area())
print(shape2.circumference())
print(shape3.volume())
print(shape3.area())
print(shape3.circumference())
shape4: Shape2D = None
if random.randint(0, 1) == 0:
    shape4 = Square(10)
else:
    shape4 = Triangle(10, 5)
print(shape4)
print(shape4.area())
print(shape4.circumference())

shapes: list[Shape2D] = [Square(10), Triangle(10, 5), Circle(100), Square(10), Triangle(10, 5)]
for shape in shapes:
    print(shape)
    print(shape.area())
    print(shape.circumference())

volumetric_shapes: list[Shape3D] = [Cube(100), Sphere(150),Cube(200)]
for volumetric_shape in volumetric_shapes:
    print(volumetric_shape)
    print(volumetric_shape.volume())

