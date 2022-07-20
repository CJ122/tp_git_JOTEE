#!/usr/bin/env python3

def add(a, b):
  x = a + b 
  return x

import sys
print (sys.argv)
if len(sys.argv) == 3:
  a =float(sys.argv[1])
  b =float(sys.argv[2])
if len(sys.argv) > 3:
  print ("Invalid number of arguments")
elif len(sys.argv) == 2:
 print ("An argument is missing.")
 a =float(sys.argv[1])
 b = float(input("Please enter argument 2: "))
print ("The sum is:", add(a, b))

