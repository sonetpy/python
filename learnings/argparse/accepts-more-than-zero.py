"""
Scenario-3: Argument expects 0 or more values
Similar to (+) sign, you can use asterisk (*) with nargs to define zero or more values to a certain argument. We will update our script from Scenario-2 to use nargs='*' for --num argument and re-run the script:
"""
import argparse
parser=argparse.ArgumentParser("accepts more than 1 arguments")
parser.add_argument('--num', dest='num', type=int, nargs='*', help="define integers to perform addition" )
args=parser.parse_args()
k = 0
for i in args.num:
    k = k + i
    #print(i, ' + ', '=', end=" ")
    print(str(i), '+'.join(str(i)))
    
print (k)
print('%s = %d' % (' + '.join([str(i) for i in args.num]),sum(args.num),))