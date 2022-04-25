import argparse

parser = argparse.ArgumentParser()
"""
action='store_true' : The action set to store_true will store the argument as True , if present.

dest = 'abhinav' : The dest option of the add_argument gives a name to the argument. If not given, it is inferred from the option.
"""
parser.add_argument('-q', '--quiet', action='store_true', dest='abhinav', help='Suppress Output')
parser.add_argument('-v', '--verbose', action='store_true', dest='bhai' , help='Verbose Output')
args = parser.parse_args()

print('Quiet mode is %s.' % args.abhinav)
print(args.bhai)
