#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """This Rectangle class inherits from Base class and contains various methods used for performing various functions as can be observed from the code."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the top-left corner of the rectangle (default is 0).
        - y (int): The y-coordinate of the top-left corner of the rectangle (default is 0).
        - id: The identifier of the rectangle (default is None).

        Raises:
        - TypeError: If width, height, x, or y is not an integer.
        - ValueError: If width or height is less than or equal to 0, or if x or y is less than 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for the width property."""
        return self.__width

    @property
    def height(self):
        """Getter method for the height property."""
        return self.__height

    @property
    def x(self):
        """Getter method for the x property."""
        return self.__x

    @property
    def y(self):
        """Getter method for the y property."""
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setter method for the width property.

        Parameters:
        - value (int): The new value for the width.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.

        Parameters:
        - value (int): The new value for the height.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter method for the x property.

        Parameters:
        - value (int): The new value for the x-coordinate.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter method for the y property.

        Parameters:
        - value (int): The new value for the y-coordinate.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle representation using '#' characters based on its width and height."""
        for i in range(self.__y):
            print(" " * self.__x + "#" * self.__width)
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Overrides the default string representation of the object.

        Returns:
        - str: A formatted string representing the Rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
