#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

fourNumbers = input('Write four numbers separated by commas')
target = []

def multiplyToOthers(index):

  results = [4]

  for x in range(0,4):
    if (index != x):
      result = fourNumbers[index] * fourNumbers[x]
      results.insert(x, result)
    else: 
      results.insert(x, -1)

  return results

i = 0
currentMax = 0

while (i < 4):
  
  ml = multiplyToOthers(i)
  ml.append(currentMax)

  currentMax = max(ml)

  i = i + 1

print 'Maximum multiplication number for two numbers in {0} tuple is {1}'.format(fourNumbers, currentMax)
