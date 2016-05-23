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

def distance(a, b):
  subs = substractVectors(a, b)
  return normalize(subs[0], subs[1])

print distance(xy, x2y2)
