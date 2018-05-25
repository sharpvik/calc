# DOMCA -- Dominican Calculator (Beta)

Extended functionality. Specialized math functions added.

## Progress

| Filename          | Status           |
|:-----------------:|:-----------------|
| *do.py*           | DONE             |
| *pars.py*         | DONE             |
| *prefuncs.py*     | in process...    |
| *rpn.py*          | in process...    |
| *synt.py*         | in process...    |

## How to Use

1. Clone or Download as ZIP;
2. Then, there are two ways to use it:
    + Input / output through the Terminal or
    + Read / write to a file

### Terminal Method

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

### File Read/Write Method

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

If you do want to read and write to a file, make it `-f` for *file*. Now, you have to remember that in this case you will also have to provide the full path to a source file and the full path to an output file as the third and the fourth argument when invoking DOMCA (see examples in **File Read/Write Method**). If your source file is located in the same folder with *do.py*, you don't have to specify the path to it -- just the filename and its extention (same goes for output file).

### Proc

The second parameter `proc` tells the function whether you want your expression solved or transformed into Reversed Polish Notation (aka Postfix or RPN).

If you want DOMCA to simply solve your expression, make it `-s` for *solve*. If you want to transform your equation into RPN, make it `-c` for *compile*.

## Available Operations

### Table

| Operation         |  Sign  | Operation         |  Sign  |
|:-----------------:|:------:|:-----------------:|:------:|
| Add               |  +     | Power             | ^      |
| Subtract          |  -     | Integral Division | //     |
| Multiply          |  *     | Factorial         | !      |
| Divide            |  /     | Prime Check       | $      |
| Modulo            |  %     | Comment           | #      |

### File Format

While playing with DOMCA in your Terminal, the only thing you can do is write your expression and see what DOMCA prints back. However remember, you can also create files with supported expressions, make DOMCA read it and write solutions to another file (see *File Read/Write Method); and when you're giving DOMCA an input file instead of using it from the Terminal you get somewhat expanded functionality.

#### Speech Marks

Since you are writing your expression to a file, you don't have to put it in speech marks. How cool is that!

#### Spacing

Empty lines will be displayed in the output file which allows you to group related expressions visually.

#### Commenting

You can comment your expressions. To do that, put hash (#) symbol as a first character in line and write your comment after that.

```txt
# comment

# prime checks
19 $
30 $
```

## Contact

For any personal or business enquiries:

+ Email: *sharp.vik@gmail.com*
+ [Twitter](https://twitter.com/sharp_vik)
+ [VK](https://vk.com/perigrinus)
+ [Instagram](https://www.instagram.com/viktooooor)