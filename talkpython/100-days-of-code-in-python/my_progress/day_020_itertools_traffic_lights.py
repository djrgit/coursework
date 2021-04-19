#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
import itertools
import random


colors = 'Green Yellow Red'.split()

light_cycle = itertools.cycle(colors)


def rg_timer():
    return random.randint(3,7)

def light_rotation(light_cycle):
    for color in light_cycle:
        if color == 'Green':
            print(f'Go!  The light is {color}')
            sleep(rg_timer())
        elif color == 'Yellow':
            print(f'Caution!  The light is {color}')
            sleep(rg_timer())
        elif color == 'Red':
            print(f'STOP!  The light is {color}')
            sleep(rg_timer())


if __name__ == '__main__':
    light_rotation(light_cycle)
