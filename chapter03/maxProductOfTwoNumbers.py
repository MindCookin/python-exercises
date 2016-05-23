#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

fourNumbers = input('Write four numbers separated by commas')
target = []

def multiplyToNext(index, maximum):

  for x in range(index,4):
      print ('operation! {0} * {1}'.format(fourNumbers[index],fourNumbers[x]))
      result = max(fourNumbers[index] * fourNumbers[x], maximum)

  return result

i = 0
currentMax = 0

while (i < 3):
  currentMax = max(multiplyToNext(i, currentMax), currentMax)
  i = i + 1

print 'Maximum multiplication number for two numbers in {0} tuple is {1}'.format(fourNumbers, currentMax)
