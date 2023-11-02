# 0x02. Python - Import & Modules

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Tasks](#tasks)
    1. [Import a simple function from a simple file](#task-0-import-a-simple-function-from-a-simple-file)
    2. [My first toolbox!](#task-1-my-first-toolbox)
    3. [How to make a script dynamic!](#task-2-how-to-make-a-script-dynamic)
    4. [Infinite addition](#task-3-infinite-addition)
    5. [Who are you?](#task-4-who-are-you)
    6. [Everything can be imported](#task-5-everything-can-be-imported)

## Introduction

This project is designed to help you understand the basics of Python programming related to importing modules and functions, using command line arguments, and maintaining code quality. It includes several tasks that will test your understanding and coding skills.

## Learning Objectives

By completing this project, you are expected to achieve the following learning objectives:

### General

- Understand why Python programming is awesome.
- Learn how to import functions from another file.
- Know how to use imported functions.
- Learn how to create a module.
- Understand how to use the built-in function `dir()`.
- Know how to prevent code in your script from being executed when imported.
- Learn how to use command line arguments with your Python programs.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should use `pycodestyle` (version 2.8.*) for style compliance.
- All your files must be executable.
- The length of your files will be tested using `wc`.

## Tasks

### Task 0: Import a simple function from a simple file

Write a program that imports the function `add(a, b)` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

You have to use the `print` function with string format to display integers.
You have to assign:
- the value `1` to a variable called `a`
- the value `2` to a variable called `b`
and use those two variables as arguments when calling the function `add` and print.

`a` and `b` must be defined on 2 different lines: `a = 1` and another `b = 2`.

Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

You can only use the word `add_0` once in your code.

You are not allowed to use `*` for importing or `__import__`.

Your code should not be executed when imported.

### Task 1: My first toolbox!

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

Do not use the function `print` (with string format to display integers) more than 4 times.

You have to define:
- the value `10` to a variable `a`
- the value `5` to a variable `b`
and use those two variables only as arguments when calling functions (including print).

`a` and `b` must be defined on 2 different lines: `a = 10` and another `b = 5`.

Your program should call each of the imported functions.

The word `calculator_1` should be used only once in your file.

You are not allowed to use `*` for importing or `__import__`.

Your code should not be executed when imported.

### Task 2: How to make a script dynamic!

Write a program that prints the number of and the list of its arguments.

The output should be:

- Number of argument(s) followed by argument (if the number is one) or arguments (otherwise), followed by
- `:` (or `.` if no arguments were passed) followed by a new line, followed by (if at least one argument),
- one line per argument:
    - the position of the argument (starting at 1) followed by `:`, followed by the argument value and a new line.

Your code should not be executed when imported.

The number of elements of `argv` can be retrieved by using: `len(argv`.

You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

### Task 3: Infinite addition

Write a program that prints the result of the addition of all arguments.

The output should be the result of the addition of all arguments, followed by a new line.

You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers).

Your code should not be executed when imported.

### Task 4: Who are you?

Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally).

You should print one name per line, in alpha order.

You should print only names that do not start with `__`.

Your code should not be executed when imported.

Make sure you are running your code in Python 3.8.x (hidden_4.pyc has been compiled with this version).

### Task 5: Everything can be imported

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

You are not allowed to use `*` for importing or `__import__`.

Your code should not be executed when imported.
### advanced taske
three advanced taskes
