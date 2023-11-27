# 0x08. Python - More Classes and Objects

## Overview

This project introduces the concept of Object-Oriented Programming (OOP) in Python, focusing on classes and objects. The tasks involve creating a `Rectangle` class with various properties and methods, such as calculating area and perimeter, implementing a custom string representation, handling instance deletion, and comparing rectangles based on their area.

## Learning Objectives

After completing this project, you should be able to:

- Understand the principles of Object-Oriented Programming (OOP)
- Define and use classes and instances in Python
- Work with instance attributes, class attributes, and properties
- Implement class methods, static methods, and special methods such as `__str__` and `__repr__`
- Handle instance deletion and use static methods for comparisons
- Apply good coding practices, including PEP 8 style guide

## Project Structure

The project contains the following files:

1. **0-rectangle.py**: Defines an empty class `Rectangle`.

2. **1-rectangle.py**: Extends the `Rectangle` class with private width and height attributes, along with a custom initialization method.

3. **2-rectangle.py**: Enhances the `Rectangle` class with public methods for calculating area and perimeter.

4. **3-rectangle.py**: Improves the `Rectangle` class by adding a custom string representation using `__str__` and `__repr__` methods.

5. **4-rectangle.py**: Extends the `Rectangle` class to support instance representation using `__repr__` for recreation using `eval()`.

6. **5-rectangle.py**: Adds a message to be displayed when an instance of `Rectangle` is deleted using `__del__`.

7. **6-rectangle.py**: Introduces a class attribute `number_of_instances` to count the number of instances created.

8. **7-rectangle.py**: Extends the `Rectangle` class with a class attribute `print_symbol` to customize the string representation character.

9. **8-rectangle.py**: Adds a static method `bigger_or_equal` to compare two rectangles based on their area.

10. **9-rectangle.py**: Introduces a class method `square` that creates a square instance of `Rectangle`.

11. advanveds: 1 advanved task

## Usage

To test the functionality of each task, you can create instances of the `Rectangle` class in separate test scripts. For example:

```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
