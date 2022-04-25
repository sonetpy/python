"""
The Python argparse module provides a special class that can be sent to the type keyword argument of add_argument, which is argparse.FileType.

The argparse.FileType class expects the arguments that would be sent to Python's open function, excluding the filename (which is what is being provided by the user invoking the program). If you are opening the file for reading, this may be nothing. open defaults to opening files only for reading. However, any arguments after the initial positional argument to open can be provided to FileType, and they will be passed on to open.
"""
#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file',
                    type=argparse.FileType('r'),
                    dest='myfile',
                    default='/etc/hosts', help='The config file to use')
args = parser.parse_args()
print(args.myfile.read())
"""
This would read from /tmp/file by default, but allow you to specify a different file to read from using the --file argument. Rather than providing these options as text and forcing you to open the file yourself, you will simply be provided with an open file object:
"""