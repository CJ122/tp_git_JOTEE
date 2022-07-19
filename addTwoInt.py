#!/usr/bin/env python3

def add(a, b):
  x = a+b
  return x

import sys
print (sys.argv)
a = float(sys.argv[1])
b = float(sys.argv[2])
print ("The sum is:", add(a,b))

