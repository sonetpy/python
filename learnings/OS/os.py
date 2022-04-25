import os
print("os.uname() is used to print the 'uname -a': ", os.uname())
print("\nreturns the current directory os.getcwd() : ", os.getcwd())
print("\nreturns True if dir exists os.path.isdir os.path.isdir: ", os.path.isdir('testdir'))
print("\nreturns True if file exists os.path.isfile : ", os.path.isfile('accounts.txt')) # returns True if file exists
print("\nreturns True if link exists os.path.islink(): ", os.path.islink('accounts.txt')) # returns True if link exists
print("\nreturns True if dir exists (full pathname or filename)os.path.exists() ", os.path.exists('accounts.txt'))
print("returns size of a file without opening it.  os.path.getsize(<filename>): ", os.path.getsize('accounts.txt')) #returns size of a file without opening it.
print("os.path.abspath() absolute path of the file :", os.path.abspath('accounts.txt'))
