#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """This Rectangle class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function writes the class Rectangle that inherits from Base"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.__width} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.__width} must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be >= 0")
        self.__y = value

