#!/usr/bin/env python
# -*- coding: utf-8 -*-

def toSeconds(h, m, s):
  return h * 3600 + m * 60 + s

def toHoursMinutesAndSeconds(s):
  hours = s / 3600
  minutes = s % 3600 / 60
  seconds = s % 3600 % 60
  return (hours, minutes, seconds)

print "10h 30m and 50s are {0} seconds".format(toSeconds(10, 30, 50))
print toHoursMinutesAndSeconds(37850)
