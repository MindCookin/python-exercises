#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

print 'Insert one points, separated with commas: '
xy = input('Insert first point: ')
x2y2 = input('Insert second point: ')

def substractVectors(a, b):
  return (a[0] - b[0], a[1] - b[1])

def normalize(x, y):
  return math.sqrt(x**2 + y**2)

print normalize(*xy)
print normalize(*x2y2)
