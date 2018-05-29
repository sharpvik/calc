    # imports
from math import sqrt





def prime_check(n):                     # n(int) -- any positive number; --> function returns True or False
    if not isinstance(n, int):
        raise ValueError("prime_check() arg must be of type int")
    elif n < 0:
        raise ValueError("prime_check() arg must be a positive number")
    else:
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
    if not isinstance(n, int):
        raise ValueError("factorial() arg must be of type int")
    elif n < 0:
        raise ValueError("factorial() arg must be a positive number")
    elif n < 2:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


def nPr(n, r):      # n(int) -- number of items; r(int) -- number of positions; --> function returns number of permutations of n elements for r positions;
    return int( factorial(n) // factorial(n - r) )


def nCr(n, r):      # n(int) -- number of items; r(int) -- number of positions; --> function returns number of combinations of n elements for r positions;
    return int( factorial(n) // ( factorial(n - r) * factorial(r) ) )
