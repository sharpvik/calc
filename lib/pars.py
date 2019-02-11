    # parser
from string import digits



LEXEMS = {
    'digits'    : set(digits),
    'operators' : set(['+', '-', '*', '/', '//', '%', '^', '!', '$', '(', ')']),
}



def identify_char(char):
    if char in LEXEMS['digits']:
        return 'number'
    if char in LEXEMS['operators']:
        return 'operator'
    else:
        return None
    

def pars(exp):
    # validate initial expression
    if len(exp) == 0:
        return None
    
    # set main variables    
    exp = ''.join( exp.split() ) + '\r'
    state = None
    toks = list()
    current_tok = str()
    
    # start the loop
    for char in exp:
        # endline reached
        if char == '\r':
            if state == 'number':
                toks.append(current_tok)
                return toks
            else:
                raise ValueError('Expression incomplete. Operator cannot be the last token.')
        
        # first char hit
        if state is None:
            char_identity = identify_char(char)
            if char_identity is not None:
                state = char_identity
                current_tok += char
                continue
            else:
                raise ValueError('Invalid expression. Unregistered symbol was detected.')
                return None
        
        # general case
        char_identity = identify_char(char)
        
        # validate char
        if char_identity is None:
            raise ValueError('Invalid expression. Unregistered symbol was detected.')
            return None
            
        # tok is a bracket
        if char in '()':
            toks.append(current_tok)
            toks.append(char)
            current_tok = str()
            state = None
        
        # tok continues
        elif char_identity == state:
            current_tok += char
        
        # state change
        else:
            toks.append(current_tok)
            current_tok = char
            state = char_identity

