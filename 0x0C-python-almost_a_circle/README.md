# Rectangle Class Project

This project includes the implementation of two Python classes: `Base` and `Rectangle`. The `Rectangle` class inherits from the `Base` class and introduces additional functionality for managing rectangles.

## Base Class

### File Structure

- Folder: `models`
  - File: `__init__.py` (empty file to make the folder a Python package)
  - File: `base.py`

### Base Class Overview

The `Base` class serves as the foundation for other classes in the project. It includes the following features:

- Private class attribute `__nb_objects` for managing unique identifiers.
- Constructor `__init__(self, id=None)` for initializing instances with a unique identifier.
- `__nb_objects` is incremented when an instance is created without an explicit ID.

## Rectangle Class

### File Structure

- Folder: `models`
  - File: `rectangle.py`

### Rectangle Class Overview

The `Rectangle` class inherits from the `Base` class and introduces features for managing rectangles:

- Private instance attributes with public getter and setter methods: `__width`, `__height`, `__x`, and `__y`.
- Constructor `__init__(self, width, height, x=0, y=0, id=None)` for initializing rectangle instances with specific attributes.
- Validation in setter methods and instantiation:
  - Type validation: Raises `TypeError` if the input is not an integer.
  - Value validation (width and height): Raises `ValueError` if width or height is <= 0.
  - Value validation (x and y): Raises `ValueError` if x or y is < 0.

## Usage Example

```python
from models.rectangle import Rectangle

# Create a rectangle instance
rectangle1 = Rectangle(10, 5)

# Access attributes using getters
print(rectangle1.width)  # Output: 10
print(rectangle1.height)  # Output: 5

# Update attributes using setters
rectangle1.width = 15
rectangle1.height = 8

# Access updated attributes
print(rectangle1.width)  # Output: 15
print(rectangle1.height)  # Output: 8
