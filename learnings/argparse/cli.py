"""
The argparse module is part of the Python standard library, and lets your code accept command line arguments. 
This makes your code easy to configure at run-time. There are multiple ways to do this in Python, but argparse is the most powerful with minimal additional code required.
This article is a collection of example code snippets — I wrote it because the official documentation is quite heavy-going, and couldn’t find a suitable quick reference.

Basic usage
-------------------
There are four basic steps to using argparse in your code:
1.	import the argparse module;
2.	create the parser;

Setting up a Parser:
--------------------------
The first step when using argparse is to create a parser object and tell it what arguments to expect. The parser can then be used to process the command line arguments when your program runs.

The parser class is ArgumentParser. The constructor takes several arguments to set up the description used in the help text for the program and other global behaviors or settings.


import argparse
parser = argparse.ArgumentParser(description="Maths hai bhaiya ji")

3.	add arguments;

Defining Arguments
-----------------------
argparse is a complete argument processing library. Arguments can trigger different actions, specified by the action argument to add_argument(). Supported actions include storing the argument (singly, or as part of a list), storing a constant value when the argument is encountered (including special handling for true/false values for boolean switches), counting the number of times an argument is seen, and calling a callback.

The default action is to store the argument value. In this case, if a type is provided, the value is converted to that type before it is stored. If the dest argument is provided, the value is saved to an attribute of that name on the Namespace object returned when the command line arguments are parsed.

4.  parse the arguments.

Parsing a Command Line
---------------------------
Once all of the arguments are defined, you can parse the command line by passing a sequence of argument strings to parse_args(). By default, the arguments are taken from sys.argv[1:], but you can also pass your own list. The options are processed using the GNU/POSIX syntax, so option and argument values can be mixed in the sequence.

The return value from parse_args() is a Namespace containing the arguments to the command. The object holds the argument values as attributes, so if your argument dest is "myoption", you access the value as args.myoption.

"""

import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x/args.y

    else:
        return "Baba, something went wrong"

if __name__ == '__main__':
    # ArgumentParser is a CLASS in argparse file in Python
    # You can use the argparse module to write a command-line interface that accepts a positional argument. 
    parser = argparse.ArgumentParser(description="Maths hai bhaiya ji")
    parser.add_argument('--x', type=float, default=1.0, help="Enter first num, This is a utility for calculation. Please contact Abhinav")
    parser.add_argument('--y', type=float, default=3.0, help="Enter second num, This is a utility for calculation. Please contact Abhinav")
    parser.add_argument('--o', type=str, default="add", help="This is a utility for calculation. Please contact Abhinav")

    args = parser.parse_args()
    # This will print the output of function converted into string and then print.
    sys.stdout.write(str(calc(args)))