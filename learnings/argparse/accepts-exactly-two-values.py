import argparse
parser = argparse.ArgumentParser(description="Exactly two values game")
#  nargs=2 means number of arguments 
parser.add_argument('--value', default=[1-100], dest='range',help='Define the range. Default is 1-100',type=int, nargs=2)
args = parser.parse_args()
print(f'The defined range is {args.range[0]}-{args.range[1]}')