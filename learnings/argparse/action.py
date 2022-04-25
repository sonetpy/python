# Using "action" with ArgumentParser
"""
ArgumentParser objects associate command-line arguments with actions. These actions can do just about anything with the command-line arguments associated with them, though most actions simply add an attribute to the object returned by parse_args().

Any of six built-in actions can be triggered when an argument is encountered:

store: Save the value, after optionally converting it to a different type. This is the default action taken if none is specified explicitly.
store_const: Save a value defined as part of the argument specification, rather than a value that comes from the arguments being parsed. This is typically used to implement command-line flags that are not boolean values.
store_true/store_false: Save the appropriate boolean value. These actions are used to implement Boolean switches.
append: Save the value to a list. Multiple values are saved if the argument is repeated.
append_const: Save a value defined in the argument specification to a list.
version: Print the version details about the program and then exit.
In this example we have defined all the possible actions which can be used with ArgumentParser():
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store', dest='simple_value', help='Store a simple value')
parser.add_argument('-c', action='store_const', dest='constant_value', const='value-to-store', help='Store a constant value')
parser.add_argument('-t', action='store_true', default=False, dest='boolean_t', help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=True, dest='boolean_f', help='Set a switch to false')
parser.add_argument('-a', action='append', dest='collection', default=[], help='Add repeated values to a list')
parser.add_argument('-A', action='append_const', dest='const_collection', const='value-1-to-append', default=[], help='Added different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection', const='value-2-to-append', help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()
print('simple_value     = {!r}'.format(results.simple_value))
print('constant_value   = {!r}'.format(results.constant_value))
print('boolean_t        = {!r}'.format(results.boolean_t))
print('boolean_f        = {!r}'.format(results.boolean_f))
print('collection       = {!r}'.format(results.collection))
print('const_collection = {!r}'.format(results.const_collection))