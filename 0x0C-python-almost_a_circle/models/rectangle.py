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
        if not isinstance(self.__width, int):
            raise TypeError(f"{self.__width} must be an integer")
        if self.__width <= 0:
            raise ValueError(f"{self.__width} must be > 0")
        return self.__width

    @property
    def height(self):
        if not isinstance(self.__height, int):
            raise TypeError(f"{self.__height} must be an integer")
        if self.__height <= 0:
            raise ValueError(f"{self.__height} must be > 0")
        return self.__height

    @property
    def x(self):
        if not isinstance(self.__x, int):
            raise TypeError(f"{self.__x} must be an integer")
        if self.__x < 0:
            raise ValueError(f"{self.__x} must be >= 0")
        return self.__x

    @property
    def y(self):
        if not isinstance(self.__y, int):
            raise TypeError(f"{self.__y} must be an integer")
        if self.__y < 0:
            raise ValueError(f"{self.__y} must be >= 0")
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value