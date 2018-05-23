# --->   DOLANG INTERPRETER   <---
# File format:      .do
# Terminal use:     $~ python do.py filename.do

#!/usr/bin/python



    # imports
from sys import argv
from lib import pars
from lib import rpn
from lib import synt





    # dominican interpreter
def do(filename):
        # open file
    file = open(filename, "r")


        # file processing (line by line)
    while True:
        line = file.readline()
        if line != '': 
            synt.synt( rpn.rpn( pars.pars(line) ) )    
            # print(line, end="")
        else: break


        # close file
    file.close()





    # invoke the do function
do(argv[1])
