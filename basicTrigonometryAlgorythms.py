#!/usr/bin/env python
 
def main():
  state = input("""
What would you lke todo:
  (1) Calculate a rectangle perimeter based on its width and height
  (2) Calculate a circle perimeter based on its radio
  (3) Calculate a sphere volume based on its radio
  (4) Calculate a rectangle's area based on it's four vertices
  (5) Calculate the hypotenuse of a triangle based on its sides
  """)

  switcher = {
    1: calcRectPerimeter,
    2: calcCircPerimeter,
    3: calcSphVolume,
    4: calcRectArea,
    5: calcHypotenuse
  }

def calcRectPerimeter():
  
def calcCircPerimeter():

def calcSphVolume():

def calcRectArea():

def calcHypotenuse():

main()
