#!/usr/bin/python3
"""text_indentation method"""


def text_indentation(text):
    """
    This function takes a string as input and prints it with indentation.
    It splits the input text using ".", "?", and ":" as delimiters and adds
    two newlines after each delimiter. The resulting text is printed.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If the input 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
