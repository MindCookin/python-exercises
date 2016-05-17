#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = input("Gimme a number: ")
total = 0

print "Complex equation"
for x in range(1, n + 1):
  print "{0} - {1}".format(x, x * (x + 1) / 2)

print "Simple variable assignment"
for x in range(1, n + 1):
  total = total + x
  print "{0} - {1}".format(x, total)
