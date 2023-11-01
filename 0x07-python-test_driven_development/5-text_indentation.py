#!/usr/bin/python3
"""One function that prints a text with 2 new lines after each of these characters: ., ? and :"""
def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters: ., ? and : #.

    Args:
        a (str): text to be printed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        if char == '.' or char == '?' or char == ':':
            new_text += char + '\n\n'
        else:
            new_text += char

    print(new_text)


