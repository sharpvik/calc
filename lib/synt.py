    # imports
import prefuncs as func
from inspect import signature





    # syntax execution
def synt(postfix):
        # variables
    var = func.Stack()
    exp = list(postfix)


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
            var.push( int(tok) )
        else:                   # for operators
            if tok == '!' or tok == '$':        # for toks with 1 arg
                arg = var.pop()
                var.push( ops[tok](arg) )
            else:                               # for toks with 2 args
                arg2 = var.pop()
                arg1 = var.pop()
                var.push( ops[tok](arg1, arg2) )


        # output
    return var.pop()
