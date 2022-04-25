"""
Python ArgumentParser adds the capability to specify that an option may only be one of an enumerated set of choices. These can be handled by passing a container object as the choices keyword argument to add_argument(). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values:

This script expects any of the three values between blue, black and brown for --color argument. The default value would be blue if --color argument is not defined.
"""
print("Pass multiple choices to python argument")
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--color',
                    choices=('blue', 'black', 'brown'),
                    dest='color',
                    default='blue',
                    help='Guess my lucky color'
                    )
args = parser.parse_args()
print(f'You have chosen {args.color}')
