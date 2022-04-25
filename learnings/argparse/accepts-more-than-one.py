"""
You can use the + value with nargs which indicates that the option expects one or more values to be provided. Let us look at this example where we will perform addition using all the values provided to --num argument.

Here we have defined nargs='+' for --num argument which means --num expects one or more values.
"""
import argparse
parser=argparse.ArgumentParser("accepts more than 1 arguments")
parser.add_argument('--num', dest='num', type=int, nargs='+', help="define integers to perform addition" )
args=parser.parse_args()
k = 0
for i in args.num:
    k = k + i
    #print(i, ' + ', '=', end=" ")
    print(str(i), '+'.join(str(i)))
    
print (k)
print('%s = %d' % (' + '.join([str(i) for i in args.num]),sum(args.num),))
