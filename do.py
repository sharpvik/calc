#!/usr/bin/python



    # imports
from sys import argv
from lib import pars, rpn, synt





    # dominican interpreter
def do(mode, proc):    
        # -t mode
    if mode == '-t':
        def render():
            exp = inp.get()
            compiled = rpn.rpn( pars.pars(exp) )
            if proc == '-c': 
                answer.set( " ".join(compiled) )
            else: 
                answer.set( synt.synt(compiled) )
        
        import tkinter
        master = tkinter.Tk()
        inp = tkinter.Entry(master)
        inp.pack()
        answer = tkinter.StringVar()
        tkinter.Label(master, textvariable=answer).pack()
        answer.set("Solution will appear here.")
        submit = tkinter.Button(master, text="=", command=render)
        submit.pack()
        master.mainloop()



        # -f mode
    elif mode == '-f':
        ## open file
        infile = open(argv[3], "r")
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
do(argv[1], argv[2])