class Shape2D:
    def area(self) -> float:
        pass

    def circumference(self) -> float:
        pass


class Shape3D:
    def volume(self) -> float:
        pass


class Square(Shape2D):
    def __init__(self, side: float) -> None:
        self.__side = side

    @property
    def side(self) -> float:
        return self.__side

    def area(self) -> float:
        return self.__side * self.__side

    def circumference(self) -> float:
        return 4 * self.__side

    def __str__(self) -> str:
        return f"Square(side={self.__side})"


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
        return self.__base * self.__height / 2.0

    def circumference(self) -> float:
        return self.__base * 2 + self.__height * 2

    def __str__(self) -> str:
        return f"Triangle(base={self.__base}, height={self.__height})"


class Cube(Shape2D, Shape3D):
    def __init__(self, side: float) -> None:
        self.__side = side

    def volume(self) -> float:
        return self.__side * self.__side * self.__side

    def area(self) -> float:
        return 6 * self.__side * self.__side

    def circumference(self) -> float:
        return 12 * self.__side

    def __str__(self) -> str:
        return f"Cube(side={self.__side})"
