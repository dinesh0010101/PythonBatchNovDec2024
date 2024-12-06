#!/usr/bin/python3

"""
Purpose : Basic PEP 8 guidlines and
    shebang line

    PEP - Python Enhancement Proposal
    PEP 8 - Coding style guide

This is docstring

"""


# print as a statment in python 2
# print "Hello, World"

# print as a function in python 2 & 3
print("Hello, World!")
print(True)
print("True",123,None)


def wishes(name):
    wish = "How are you {0}?",format(name)
    print(wish)

    wishes("Dinesh")

    