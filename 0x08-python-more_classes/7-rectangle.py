#!/usr/bin/python3
""" class Rectangle that defines a Rectangle """


class Rectangle:
    """class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a Rectangle
        args1: width = width of Rectangle
        args2: height = height of Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property   # Getter
    def width(self):
        """get the width of the Rectangle"""
        return (self.__width)

    @width.setter   # Setter
    def width(self, value):
        """set and validate the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property   # Getter
    def height(self):
        """get the height of the Rectangle"""
        return (self.__height)

    @height.setter   # setter
    def height(self, value):
        """set and validate the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the Rectangle perimeter"""
        if self.__width <= 0 or self.__height <= 0:
            perimeter = 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """ print the rectangle with the character # """
        string = ""
        if self.__height != 0 and self.__width != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message "Bye rectangle..."
        when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
