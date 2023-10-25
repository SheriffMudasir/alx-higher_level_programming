#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:.f}".format(divide))
    return divide
