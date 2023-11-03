# 0x03. Python - Data Structures: Lists, Tuples

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
**Python Scripts**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

**C**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called lists.h
- Don't forget to push your header file
- All your header files should be include guarded

## Quiz Questions
Great! You've completed the quiz successfully! Keep going!

## Tasks

### 0. Print a list of integers (mandatory)

Write a function that prints all integers of a list.

**Prototype:** `def print_list_integer(my_list=[]):`
**Format:** one integer per line.
**You are not allowed to import any module.**
**You can assume that the list only contains integers.**
**You are not allowed to cast integers into strings.**
**You have to use str.format() to print integers.**

Example:
```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
# Python - Data Structures: Lists, Tuples

This project includes various tasks related to Python data structures, lists, and tuples. Each task has its own function to be implemented, and the required functionality and constraints are outlined below.

## Task 0: Secure access to an element in a list (mandatory)

Write a function that retrieves an element from a list like in C.

**Prototype:** `def element_at(my_list, idx):`
- If `idx` is negative, the function should return `None`.
- If `idx` is out of range (> the number of elements in `my_list`), the function should return `None`.
- You are not allowed to import any module.

## Task 1: Replace element (mandatory)

Write a function that replaces an element of a list at a specific position (like in C).

**Prototype:** `def replace_in_list(my_list, idx, element):`
- If `idx` is negative, the function should not modify anything and return the original list.
- If `idx` is out of range (> the number of elements in `my_list`), the function should not modify anything and return the original list.
- You are not allowed to import any module.

## Task 2: Print a list of integers... in reverse! (mandatory)

Write a function that prints all integers of a list, in reverse order.

**Prototype:** `def print_reversed_list_integer(my_list=[]):`
- Format: one integer per line.
- You are not allowed to import any module.
- You can assume that the list only contains integers.
- You are not allowed to cast integers into strings.
- You have to use `str.format()` to print integers.

## Task 3: Replace in a copy (mandatory)

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

**Prototype:** `def new_in_list(my_list, idx, element):`
- If `idx` is negative, the function should return a copy of the original list.
- If `idx` is out of range (> the number of elements in `my_list`), the function should return a copy of the original list.
- You are not allowed to import any module.

## Task 4: Can you C me now? (mandatory)

Write a function that removes all characters 'c' and 'C' from a string.

**Prototype:** `def no_c(my_string):`
- The function should return the new string.
- You are not allowed to import any module.
- **You are not allowed to use `str.replace()`.

## Task 5: Lists of lists = Matrix (mandatory)

Write a function that prints a matrix of integers.

**Prototype:** `def print_matrix_integer(matrix=[[]]):`
- You are not allowed to import any module.
- You can assume that the list only contains integers.
- You are not allowed to cast integers into strings.
- You have to use `str.format()` to print integers.

## Task 6: Tuples addition (mandatory)

Write a function that adds 2 tuples.

**Prototype:** `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
  - The first element should be the addition of the first element of each argument.
  - The second element should be the addition of the second element of each argument.
- You are not allowed to import any module.
- You can assume that the two tuples will only contain integers.
- **If a tuple is smaller than 2, use the value 0 for each missing integer.**
## Task 7: Tuples Addition (mandatory)

Write a function that adds two tuples.

**Prototype:** `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
  - The first element is the addition of the first element of each argument.
  - The second element is the addition of the second element of each argument.
- You are not allowed to import any module.
- You can assume that the two tuples will only contain integers.
- If a tuple is smaller than 2, use the value 0 for each missing integer.
- If a tuple is bigger than 2, use only the first 2 integers.

## Task 8: More Returns! (mandatory)

Write a function that returns a tuple with the length of a string and its first character.

**Prototype:** `def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to None.
- You are not allowed to import any module.

## Task 9: Find the Max (mandatory)

Write a function that finds the biggest integer in a list.

**Prototype:** `def max_integer(my_list=[]):`
- If the list is empty, return None.
- You can assume that the list only contains integers.
- You are not allowed to import any module.
- You are not allowed to use the built-in max() function.

## Task 10: Only by 2 (mandatory)

Write a function that finds all multiples of 2 in a list.

**Prototype:** `def divisible_by_2(my_list=[]):`
- Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2.
- The new list should have the same size as the original list.
- You are not allowed to import any module.

## Task 11: Delete At (mandatory)

Write a function that deletes the item at a specific position in a list.

**Prototype:** `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing changes (returns the same list).
- You are not allowed to use pop().
- You are not allowed to import any module.

## Task 12: Switch (mandatory)

Complete the source code to switch the values of two variables, `a` and `b`.

## Task 13: Linked List Palindrome (mandatory)

Write a function in C that checks if a singly linked list is a palindrome.

**Prototype:** `int is_palindrome(listint_t **head);`
- Return: 0 if it is not a palindrome, 1 if it is a palindrome.
- An empty list is considered a palindrome.
## Advanced taskes
1 advanced taske

The project directory contains the necessary C source code and header file to implement the is_palindrome function.

Each task should be implemented in its respective Python file and C file (if applicable), following the provided prototypes and constraints.

Feel free to navigate to the specific task directories for more details and source code implementation.

For additional information and examples, refer to the GitHub repository for this project.

**GitHub repository:** [alx-higher_level_programming](https://github.com/USERNAME/alx-higher_level_programming)
**Directory:** 0x03-python-data_structures
