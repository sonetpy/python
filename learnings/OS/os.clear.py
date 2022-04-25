# this will clear off your screen
import os
import platform
l = platform.system()
# for Linux OS
if (l == 'Linux'):
    os.system("clear")
    print("Ths is Linux")
# for windows OS
if (l == 'Windows'):
    os.system("cls")
    print("This is Windows")

