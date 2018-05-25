    # imports
import prefuncs as func
from stackD import Stack





    # reverse polish notation
def rpn(toks):
        # variables
    stack = Stack()
    exp = list(toks)
    postfix = list()    # output list


        # operators
    ops = [ '+', '-', '*', '/', '//',
            '%', '^', '!', '$',
            '(', ')' ]


        # order of precedence
    prec = {
        1   : [ "!" ],
        2   : [ "^" ],
        3   : [ "*", "/", "//", "%" ],
        4   : [ "+", "-" ],
        5   : [ "$" ]
    }


        # functions
    def higher_prec(test, against):
        test_level = int()
        against_level = int()

        for level in prec:
            if test in prec[level]: test_level = level
            if against in prec[level]: against_level = level

        return test_level < against_level


        # rpn formation
    for tok in exp:
        if tok not in ops:          # for numbers
            postfix.append(tok)
        else:                       # for operators
            pass

    
    while not stack.is_empty():     # empty the stack
        postfix.append( stack.pop() )


        # output
    return postfix
