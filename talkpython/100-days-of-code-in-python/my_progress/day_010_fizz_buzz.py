#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'Fizz Buzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n

