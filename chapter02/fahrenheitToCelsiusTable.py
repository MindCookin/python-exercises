#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getCelsius(f):
  return (f-32) * 5/ 9

for index in range(10, 130, 10):
  fahrenheit = index
  print "{0}ºF are {1}ºC".format(fahrenheit, getCelsius(fahrenheit))
