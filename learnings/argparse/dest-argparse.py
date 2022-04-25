import math
import argparse

#create an ArgumentParser object
parser = argparse.ArgumentParser()
#Add arguments
#positional argument
parser.add_argument('foobar')
#optional argument 1
parser.add_argument('-r', '--radius-circle')
# optional argument 2
parser.add_argument('-x', '-y')
parser.add_argument('-n','--newarg', dest = 'sonu')
obj = parser.parse_args('9 -r 1 -x 2 -n 5'.split())
print(obj)                     