#!/usr/bin/env python
# -*- coding: utf-8 -*-

from secondsAndHours import toSeconds

firstDate = input('Gimme a date: ')
secondDate = input('Gimme another date: ')

print toSeconds(*firstDate) + toSeconds(*secondDate)
