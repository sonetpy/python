'''Write a Python program to print the following here document. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

myfile = open("D:/Scripts/Python/File IO/1.txt")
a = myfile.read()
myfile.close()
print (a)