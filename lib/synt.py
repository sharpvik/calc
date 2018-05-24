    # imports
from lib import prefuncs as func
from inspect import signature





    # arguments count for a function
def argc(function):
    return len( signature(function).parameters )





    # syntax execution
def synt(postfix):
        # variables
    var = func.Stack()
    exp = list(postfix)


    # operators
    ops = [ '+', '-', '*', '/', '//',
            '%', '^', '!', '$',
            '(', ')' ]


        # operators
    ops = {
            # basic
        '+'     : ( lambda a, b: a + b ),
        '-'     : ( lambda a, b: a - b ),
        '*'     : ( lambda a, b: a * b ),
        '/'     : ( lambda a, b: a / b ),
            # advanced
        '%'     : ( lambda a, b: a % b ),
        '^'     : ( lambda a, b: a ** b ),
        '//'    : ( lambda a, b: a // b ),
            # functions
        '!'     : ( lambda x: func.factorial(x) ),
        '$'     : ( lambda x: func.prime_check(x) )
    }

        # execution
    for tok in postfix:
        if tok not in ops:      # for numbers
            var.push(tok)
        else:                   # for operators
            pass


        # output
    return var.pop()
