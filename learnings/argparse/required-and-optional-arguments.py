"""
This is by design as parameters starting with - or -- are usually considered optional. All other parameters are positional parameters and as such required by design (like positional function arguments). To overcome this you can parse the arguments and store into two different objects.
"""
import argparse

parser = argparse.ArgumentParser()

# Create a new group to store required arguments
requiredName = parser.add_argument_group('required named arguments')

# Add required arguments to the parser
# metavar='TIME' : The metavar option gives a name to the expected value in error and help outputs.
requiredName.add_argument('-s', '--sleep',required=True,default=20,dest='sleep',metavar='TIME',help='Provide sleep timer',type=int)

# Add optional arguments to the parser
parser.add_argument('-q', '--quiet',action='store_true',dest='quiet',help='Suppress Output')

args = parser.parse_args()

print(f'Provided sleep value is {args.sleep}')