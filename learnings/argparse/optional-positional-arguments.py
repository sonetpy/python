print("How do we define optional and positional arguments?")
"""
The declaration for positional arguments is equivalent to the declaration for options, except that the leading hyphen is omitted.
When parse_args() is called, optional arguments will be identified by the - prefix, and the remaining arguments will be assumed to be positional.

For example, an optional argument could be created like:

>>> parser.add_argument('-f', '--foo')
while a positional argument could be created like:

>>> parser.add_argument('bar')
We will use the same code as we used in Example-5 to demonstrate nargs keyword. This script will expect integers as positional arguments which can be one or more. We will perform a SUM operation on these provided integers. We are explicitly converting the provided values into integers using type=int.

The code we used is mostly the same, except that the --num argument has been replaced with num, without the double-hyphen prefix.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num',
                    nargs='+',
                    type=int,
                    help='Provide integers to perform SUM'
                    )
args = parser.parse_args()

print('%s = %d' % (' + '.join([str(i) for i in args.num]),sum(args.num),))
