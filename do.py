# --->   DOLANG INTERPRETER   <---
# File format:      .do
# Terminal use:     $~ python do.py <mode> <proc> <input>

#!/usr/bin/python



    # imports
from sys import argv
from lib import pars
from lib import rpn
from lib import synt





    # dominican interpreter
def do(mode, proc, inp):    
        # -t mode
        
        ## process
    if mode == '-t':
        compiled = rpn.rpn( pars.pars(inp) )
        if proc == '-c': print( " ".join(compiled) )
        else: print( synt.synt(compiled) )



        # -f mode
    elif mode == '-f':
        ## open file
        infile = open(inp, "r")
        outfile = open(argv[4], "w").close()    # empty the output file
        outfile = open(argv[4], "a+")


        ## file processing (line by line)
        while True:
            line = infile.readline()
            if line != '': 
                if line[0] == '#': outfile.write(line)
                elif line == '\n': outfile.write('\n')
                else:
                    compiled = rpn.rpn( pars.pars(line) )
                    if proc == '-c': outfile.write( "{}\n".format( " ".join(compiled) ) )
                    else: outfile.write( "{}\n".format( str( synt.synt(compiled) ) ) )
            else: break


            ## close file
        infile.close()





    # invoke the do function
do( argv[1], argv[2], argv[3] )