    # imports
from math import sqrt





class Stack:                                # standard stack datatype;
    def __init__(self, element=None):
        if isinstance(element, list):
            self.storage = element
        else:
            self.storage = [element]

    def push(self, element):                # element(int / str) -- element you want to add into the Stack;
                                            # --> function returns name of the added elment;
        self.storage.append(element)
        return element

    def pop(self):                          # --> function pops the last element you put into the Stack and returns its name;
        temp = self.storage[-1]
        self.storage.pop(-1)
        return temp

    def last(self):                         # --> function returns the last value pushed to the Stack;
        return self.storage[-1]

    def length(self):                       # --> function returns number of elements in the Stack;
        return len(self.storage)

    def inside(self, element):              # element(int / str) -- name of element you want to check for;
                                            # --> function returs True if element is in the Stack, otherwise, returns False;
        return element in self.storage


def prime_check(n):                     # n(int) -- any positive number; --> function returns True or False
    a = 2
    if n == a: return True
    elif n < a: return False
    else:
        while a <= int( sqrt(n) ) + 1:
                if n % a == 0: return False
                else: a += 1
        else:
            return True


def factorial(n):   # n(int) -- any positive number; --> function returns n!;
    if n > 1: return factorial(n - 1) * n
    else: return 1
