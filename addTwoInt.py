#!/usr/bin/env python3

def Add(num1, num2):
  x = num1+num2
  return x

import sys
print (sys.argv)
if len(sys.argv) == 3:
  num1=float(sys.argv[1])
  num2=float(sys.argv[2])
if len(sys.argv) > 3:
  print ("Invalid number of arguments")
elif len(sys.argv) == 2:
 print ("An argument is missing.")
 num1=float(sys.argv[1])
 num2 = float(input("Please enter argument 2: "))
print ("The sum is:", Add(num1,num2))

