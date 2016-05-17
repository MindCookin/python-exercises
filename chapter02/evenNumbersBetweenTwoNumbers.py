#!/usr/bin/env python
# -*- coding: utf-8 -*-

first = input("Write a number: ")
second = input("Write another number: ")

for x in range(first, second):
  if (x % 2 == 0):
    print x
