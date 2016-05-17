#!/usr/bin/env python

def main():
  state = input("""
What would you lke todo:
  (1) Calculate sum, subs and mult of two numbers
  (2) Calculate multiplication table of a given number
  (3) Calculate factorial of an integer
  """)

  switcher = {
    1: calcSumSubsMult,
    2: calcMultTable,
    3: calcFactorial
  }

  switcher[state]()
  askForNext()

def askForNext():
  shouldContinue = input("""
Want another try? 
(0 to exit, any other number to continue)""")

  if shouldContinue:
    main()

def calcSumSubsMult():
  x = input("enter first number ")
  y = input("enter second number ")
  print """Sum of {0} and {1} is {2}. 
Subs of {0} and {1} is {3}. 
Mult of {0} and {1} is {4}. 
  """.format(x, y, x+y, x-y, x*y)
 
def calcMultTable():
  integer = input("enter an integer ")
  print "%d multiplication table is %d" % (integer, [integer * i for i in range(1, 10)])

def calcFactorial():
  integer = input("enter an integer ")
  print "%d factorial is %d" % (integer, reduce(lambda x, y: x*y, range(1, integer + 1)))

main()
