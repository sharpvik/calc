# DOMCA -- Dominican Calculator

Just a little experiment with Reverse Polish Notation and interpreters.

## Progress

```txt
1. **do.py**            DONE;
2. **pars.py**          DONE;
3. **prefuncs.py**      DONE;
4. **rpn.py**           *in progress...*;
5. **synt.py**          DONE;
```

## How to Use

1. Clone or Download as ZIP;
2. Then, there are two ways to use it:
    + Input / output through the Terminal or
    + Read / write to a file

### Terminal method

1. Launch Terminal in the folder;
2. Launch DOMCA as shown in the code snippet below;
3. Don't forget to put your expression in speech marks;

General invocation format:

```terminal
$~ python do.py -t <processmode> "<expression>"
```

Invocation example:

```terminal
$~ python do.py -t -c "3 + 4 * 2 - ( 3 ^ 2 )"
```

### File read/write method

1. Launch Terminal in the folder;
2. Launch DOMCA as shown in the code snippet below;
3. Specify full path to your source file including filename and its extention;
4. Specify full path to the output file including filename and its extention;
5. You must put path in speech marks if at least one of the folders in it contains spaces;

General invocation format:

```terminal
$~ python do.py -f <processmode> "<sorurce: path and filename>" "<output: path and filename>"
```

Invocation example:

```terminal
$~ python do.py -f -s "E:/examples for DOMCA/source.do" E:/outputfiles/test.txt
```

## Mode and Proc

After you write `python do.py` in your Terminal, you must specify two parameters that are responsible for the input/output mode and output format. These two parameters are called `mode` and `proc` in the `do()` function that is located in *do.py*.

So what are they?

### Mode

The `mode` tells the function how you want to input and output your expression and solution.

If you want to play with DOMCA in your Terminal and you don't need any file-tossing, just make it `-t` for *Terminal*.

If you do want to read and write to a file, make it `-f` for *file*. Now, you have to remember that in this case you will also have to provide the full path to a source file and the full path to an output file as the third and the fourth argument when invoking DOMCA (see examples in **File read/write method**). If your source file is located in the same folder with *do.py*, you don't have to specify the path to it -- just the filename and its extention (same goes for output file).

### Proc

The second parameter `proc` tells the function whether you want your expression solved or transformed into Reversed Polish Notation (aka Postfix or RPN).

If you want DOMCA to simply solve your expression, make it `-s` for *solve*. If you want to transform your equation into RPN, make it `-c` for *compile*.

## Contact

For any personal or business enquiries:

+ Email: *sharp.vik@gmail.com*
+ [Twitter](https://twitter.com/sharp_vik)
+ [VK](https://vk.com/perigrinus)
+ [Instagram](https://www.instagram.com/viktooooor)