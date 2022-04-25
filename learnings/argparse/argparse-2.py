"""
That didn’t go so well. That’s because argparse treats the options we give it as strings, unless we tell it otherwise. 
So, let’s tell argparse to treat that input as an integer:

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print(args.square**2)


That didn’t go so well. That’s because argparse treats the options we give it as strings, unless we tell it otherwise.
So, let’s tell argparse to treat that input as an integer:

"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)
