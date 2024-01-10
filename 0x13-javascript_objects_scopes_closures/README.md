# 0x13. JavaScript - Objects, Scopes and Closures

This repository contains a collection of Node.js scripts written in JavaScript, covering various concepts in JavaScript and Node.js. 

## Scripts Overview
0. **0-rectangle.js**: Defines an empty class `Rectangle` using the class notation.

1. **1-rectangle.js**: Extends the previous script by defining a `Rectangle` class with a constructor that initializes width and height attributes.

2. **2-rectangle.js**: Further extends the `Rectangle` class by adding conditions to handle cases where width or height is 0 or not a positive integer.

3. **3-rectangle.js**: Enhances the `Rectangle` class by adding an instance method `print()` that prints the rectangle using the character 'X'. It also includes methods `rotate()` and `double()`.

4. **4-rectangle.js**: Introduces a new class `Square` that inherits from the `Rectangle` class. The `Square` class includes a constructor and inherits the `print()`, `rotate()`, and `double()` methods.

5. **5-square.js**: Extends the `Square` class by adding a new method called `charPrint(c)` that prints the rectangle using the specified character `c` or defaults to 'X' if `c` is undefined.

6. **6-square.js**: Builds on the previous script, adding functionality to print a square and update its character representation.

7. **7-occurrences.js**: Defines a function `nbOccurences(list, searchElement)` that returns the number of occurrences of `searchElement` in the given list.

8. **8-esrever.js**: Implements a function `esrever(list)` that returns the reversed version of a list without using the built-in `reverse` method.

9. **9-logme.js**: Defines a function `logMe(item)` that prints the number of arguments already printed and the new argument value.

10. **10-converter.js**: Creates a function `converter(base)` that returns another function, converting a number from base 10 to the specified base.

## Instructions for Running

Each script can be executed using Node.js. For example:

```bash
guillaume@ubuntu:~/0x13$ ./10-converter.js
```