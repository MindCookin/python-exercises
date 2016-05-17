#!/usr/bin/env python

C = input("How much dollars do you need?: ")
x = input("At what interest rate?: ")
n = input("How many years?: ")

print C * (1 + x/100) ** n
