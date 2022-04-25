import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)

"""
Here is what’s happening:

We’ve added the add_argument() method, which is what we use to specify which command-line options the program is willing 
to accept. In this case, I’ve named it echo so that it’s in line with its function.

Calling our program now requires us to specify an option.

The parse_args() method actually returns some data from the options specified, in this case, echo.

The variable is some form of ‘magic’ that argparse performs for free (i.e. no need to specify which variable that value 
is stored in). You will also notice that its name matches the string argument given to the method, echo.
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

