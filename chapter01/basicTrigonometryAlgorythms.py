#!/usr/bin/env python

import math

def main():
  state = input("""
What would you lke todo:
  (1) Calculate a rectangle perimeter based on its width and height
  (2) Calculate a circle perimeter based on its radio
  (3) Calculate a sphere volume based on its radio
  (4) Calculate a rectangle's area
  (5) Calculate the hypotenuse of a triangle based on its sides
  """)

  switcher = {
    1: calcRectPerimeter,
    2: calcCircPerimeter,
    3: calcSphVolume,
    4: calcRectArea,
    5: calcHypotenuse
  }

  switcher[state]()
  askForNext()

def askForNext():
  shouldContinue = input("""
Want another try? 
(0 to exit, any other number to continue)""")
""")

  if shouldContinue:
    main()

def calcRectPerimeter():
  w = input("enter rect width ")
  h = input("enter rect height ")
  print "The perimeter of a rectangle of %d width and %d height is %d" % (w, h, w*2 + h*2)
 
def calcCircPerimeter():
  r = input("enter circle radius ")
  print "The perimeter of a circle with %d radius is %d" % (r, 2 * math.pi * r)

def calcSphVolume():
  r = input("enter sphere radius ")
  print "The volume of a sphere of %d radius id %d" % (r, 4 / 3 * math.pi * pow(r, 3))

def calcRectArea():
  w = input("enter rect width ")
  h = input("enter rect height ")
  print "The perimeter of a rectangle of %d width and %d height is %d" % (w, h, w*h)

def calcHypotenuse():
  s1 = input("enter side 1 length")
  s2 = input("enter side 2 length")
  print "The hypotenuse is %d" % math.sqrt(s1 * s1 + s2 * s2)

main()
