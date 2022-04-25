# https://www.youtube.com/watch?v=qzbZIxnFKPc
# https://www.youtube.com/watch?v=5Q9jzDL7G-8
"""
import os
def mostimpfunction():
    print("Abhinav is a coder")

print(os.listdir("/"))
print("Abhinav is great and he is king of US")
"""
# OR
"""
import os
def mostimpfunction():
    print("Abhinav is a coder")

if (__name__=="__main__"):
    print(os.listdir("/"))
    print("Abhinav is great and he is king of US")
"""
# OR
"""
import os
def mostimpfunction():
    print("Abhinav is a coder")

print(__name__)
if (__name__=="__main__"):
    print(os.listdir("/"))
    print("Abhinav is great and he is king of US")

print("\nAnother way of doing it and recommended practicse \n")
"""
# Best practicse to use main()
import os
def mostimpfunction():
    print("Abhinav is a coder")
def main():
    print(os.listdir("/"))
    print("Abhinav is great and he is king of US")

print(__name__)
if (__name__=="__main__"):
    main()