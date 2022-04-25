
import argparse
# The type=str is the variable type that is expected as an input, and the required=True parameter is a boolean for whether or not this command line field is mandatory or not.
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sleep', required=True, default=20, dest='sleep', help='Provide sleep timer', type=int)
args = parser.parse_args()

print(f'Provided sleep value is {args.sleep}')