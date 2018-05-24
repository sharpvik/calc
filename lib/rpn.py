    # imports
import prefuncs as func





    # reverse polish notation
def rpn(toks):
        # variables
    stack = func.Stack()
    exp = list(toks)
    postfix = list()    # output list


        # operators
    ops = [ '+', '-', '*', '/', '//',
            '%', '^', '!', '$',
            '(', ')' ]


        # order of precedence
    prec = {
        1   : [ "(" ],
        2   : [ "!" ],
        3   : [ "^" ],
        4   : [ "*", "/", "//", "%" ],
        5   : [ "+", "-" ],
        6   : [ "$" ]
    }


        # functions
    def higher_prec(op):
        op_level = int()
        last_level = int()

        for each in prec:
            if op in each: op_level = each
            if stack.last() in each: last_level = each

        return True if op_level < last_level else False


        # rpn formation
    for token in exp:
        if token not in ops:    # for numbers
            postfix.append(token)
        else:                   # for operators
            pass


        # output
    return postfix
