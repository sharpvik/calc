    # imports
from lib import prefuncs as func
from lib import stackD 





    # reverse polish notation
def rpn(toks):
        # variables
    stack = stackD.Stack()
    exp = list(toks)
    postfix = list()    # output list


        # operators
    ops = [ '+', '-', '*', '/', '//',
            '%', '^', '!', '$', 'nPr',
            'nCr', '(', ')' ]


        # order of precedence
    prec = {
        1   : [ '!' ],
        2   : [ '^' ],
        3   : [ 'nPr', 'nCr' ],
        4   : [ '*', '/', '//', '%' ],
        5   : [ '+', '-' ],
        6   : [ '$' ]
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
            if tok == '(':
                stack.push(tok)
            elif tok == ')':
                top_tok = stack.pop()
                while top_tok != '(':
                    postfix.append(top_tok)
                    top_tok = stack.pop()
            elif stack.peek() == '(':
                stack.push(tok)
            else:
                while not stack.is_empty() and not higher_prec( tok, stack.peek() ):
                    postfix.append( stack.pop() )
                stack.push(tok)

    
    while not stack.is_empty():     # empty the stack
        postfix.append( stack.pop() )


        # output
    return postfix
