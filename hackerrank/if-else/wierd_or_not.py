#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input().strip())
if n%2 == 1:
    print('Weird')
elif n%2 == 0 and n in range(2,5):
    print ("Not Weird")
elif n%2 == 0 and n in range(6,20):
    print('Weird')
elif n%2 == 0 and n > 20:
    print ('Not Weird')