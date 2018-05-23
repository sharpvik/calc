    # imports
from lib import prefuncs as func
from prefuncs import Stack





    # syntax execution
def synt(postfix):
        # variables
    var = Stack()
    exp = list(postfix)


    # operators
    ops = [ '+', '-', '*', '/', '//',
            '%', '^', '!', '$',
            '#', '##', '(', ')' ]


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
        '$'     : ( lambda x: func.prime_check(x) ),
            # output
        '#'     : ( lambda s: print(s) ),
        '##'    : ( lambda s: print(s, end=" ") )
    }

        # execution
    for tok in postfix:
        if tok not in ops:      # for numbers
            var.push(tok)
        else:                   # for operators
            pass
