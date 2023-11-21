# 0x06. Python - Classes and Objects

## Introduction
This project is part of the Holberton School curriculum and focuses on the fundamentals of Object-Oriented Programming (OOP) in Python. The main goal is to gain a deep understanding of classes, objects, attributes, and methods in Python, as well as the principles of encapsulation and information hiding.

## Background Context
Object-Oriented Programming (OOP) is introduced in this project, offering a new conceptual approach to programming. The provided resources give a comprehensive overview of OOP in Python, covering topics such as classes, objects, attributes, methods, and more. It is crucial to read and understand the materials in the specified order to grasp the fundamental concepts of OOP.

## Learning Objectives
After completing this project, you should be able to explain the following concepts without relying on external sources:

- Why Python programming is awesome
- What is OOP
- "First-class everything"
- What is a class
- What is an object and an instance
- The difference between a class and an object or instance
- What is an attribute
- How to use public, protected, and private attributes
- What is `self`
- What is a method
- The special `__init__` method and how to use it
- Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- The difference between an attribute and a property in Python
- The Pythonic way to write getters and setters
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to objects and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder, is mandatory
- Code should use `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`
- All modules, classes, and functions should have documentation (Python docstrings)

## Tasks
1. **My first square**
   - Write an empty class `Square` that defines a square.
   - No module import is allowed.
   - Check the provided example in `0-main.py` for expected output.

2. **Square with size**
   - Write a class `Square` that defines a square with a private instance attribute `size`.
   - Instantiation with size (no type/value verification).
   - No module import is allowed.
   - Check the provided example in `1-main.py` for expected output.
   - **Why is `size` a private attribute?** The size of a square is crucial for many operations (e.g., area computation), so as a class builder, control over the type and value of this attribute is essential.

3. **Size validation**
   - Update the `Square` class to include size validation in the instantiation process.
   - Size must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer."
   - If size is less than 0, raise a `ValueError` exception with the message "size must be >= 0."
   - No module import is allowed.
   - Check the provided example in `2-main.py` for expected output.

4. **Area of a square**
   - Update the `Square` class to include a public instance method `area()` that returns the current square area.
   - No module import is allowed.
   - Check the provided example in `3-main.py` for expected output.

5. **Access and update private attribute**
   - Extend the `Square` class to include a property `size` to retrieve it and a property setter to set it.
   - Size must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer."
   - If size is less than 0, raise a `ValueError` exception with the message "size must be >= 0."
   - No module import is allowed.
   - Check the provided example in `4-main.py` for expected output.

6. **Printing a square**
   - Enhance the `Square` class to include a public instance method `my_print()` that prints the square using the character `#`.
   - If size is equal to 0, print an empty line.
   - No module import is allowed.
   - Check the provided example in `5-main.py` for expected output.

7. **Coordinates of a square**
   - Update the `Square` class to include a private instance attribute `position`.
   - Position must be a tuple of 2 positive integers; otherwise, raise a `TypeError` exception with the message "position must be a tuple of 2 positive integers."
   - Instantiation with optional size and optional position (`def __init__(self, size=0, position=(0, 0))`).
   - Public instance methods `area()` and `my_print()` are updated to consider the position.
   - No module import is allowed.
   - Check the provided example in `6-main.py` for expected output.
8. **4 advanced tasks

## Conclusion
This project provides a hands-on experience with the principles of Object-Oriented Programming in Python. Ensure you thoroughly understand the concepts and apply them to create a well-structured and documented solution for each task. Good luck!
