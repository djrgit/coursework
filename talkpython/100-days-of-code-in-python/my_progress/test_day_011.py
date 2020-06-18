#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day_011 import word_counter

def test_word_counter():
    assert word_counter('I am a string.') == 4
