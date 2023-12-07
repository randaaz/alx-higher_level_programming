# Project: 0x0C. Python - Almost a circle

## Learning Objectives:

### General:
- Understand Unit testing and its implementation in a large project
- Learn how to serialize and deserialize a Class
- Acquire the skill to write and read a JSON file
- Understand and implement *args and **kwargs in functions
- Learn to handle named arguments in a function

### Copyright - Plagiarism:
- Develop solutions for the tasks without copying and pasting someone else’s work
- Strictly avoid publishing any content of this project
- Plagiarism is strictly forbidden and will result in removal from the program

## Requirements:

### Python Scripts:
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Mandatory `README.md` file at the root of the project folder
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- File lengths will be tested using `wc`
- Modules, classes, and functions should be documented

### Python Unit Tests:
- Allowed editors: vi, vim, emacs
- All test files inside a folder named `tests`
- Use the `unittest` module
- Test files and folders should start with `test_`
- Test file organization mirrors the project directory structure
- Execute all tests using the command: `python3 -m unittest discover tests`

## Tasks:

### Task 0: If it's not tested, it doesn't work
- Unit test all files, classes, and methods
- Validate PEP 8 compliance

### Task 1: Base class
- Create a `Base` class in `models/base.py`
- Implement a class constructor with an `id` attribute
- Manage the `id` attribute for all future classes
- Implement usage example in a main file

### Task 2: First Rectangle
- Write the `Rectangle` class that inherits from `Base`
- Implement private instance attributes for width, height, x, and y
- Define a class constructor and set the attributes accordingly
- Implement usage example in a main file

### Task 3: Validate attributes
- Add validation to setter methods and instantiation in the `Rectangle` class
- Raise appropriate exceptions for invalid input
- Implement usage example in a main file

### Task 4: Area first
- Add a public method `area` to calculate the area of the `Rectangle` instance

### Task 5: Display #0
- Add a public method `display` to print the `Rectangle` instance using '#'

### Task 6: __str__
- Override the `__str__` method in the `Rectangle` class

### Task 7: Display #1
- Improve the `display` method to consider x and y offsets

### Task 8: Update #0
- Add a public method `update` to assign arguments to attributes in the `Rectangle` class

### Task 9: Update #1
- Update the `update` method to accept key-value arguments

### Task 10: And now, the Square!
- Write the `Square` class that inherits from `Rectangle`
- Implement the class constructor and inherit attributes from `Rectangle`

### Task 11: Square size
- Add public getter and setter methods for the size attribute in the `Square` class

### Task 12: Square update
- Add a public method `update` to assign arguments to attributes in the `Square` class

### Task 13: Rectangle instance to dictionary representation
- Add a public method `to_dictionary` to return a dictionary representation of a `Rectangle` instance

### Task 14: Square instance to dictionary representation
- Add a public method `to_dictionary` to return a dictionary representation of a `Square` instance

### Task 15: Dictionary to JSON string
- Add a static method `to_json_string` in the `Base` class to return the JSON string representation of a list of dictionaries

### Task 16: JSON string to file
- Add a class method `save_to_file` in the `Base` class to write the JSON string representation of a list of instances to a file

### Task 17: JSON string to dictionary
- Add a static method `from_json_string` in the `Base` class to return the list of instances represented by a JSON string

### Task 18: Dictionary to Instance
- Add a class method `create` in the `Base` class to return an instance with attributes set from a dictionary

### Task 19: File to instances
- Add a class method `load_from_file` in the `Base` class to return a list of instances from a file

## Advanced tasks:
- 2 advanced tasks

