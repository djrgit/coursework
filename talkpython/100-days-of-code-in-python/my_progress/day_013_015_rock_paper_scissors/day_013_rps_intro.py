#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main():
    print_header()
    get_player_name()
    game_loop()


def print_header():
    print('-------------------------------------')
    print('       ROCK-PAPER-SCISSORS GAME')
    print('-------------------------------------')
    print()


def get_player_name():
    player_name = input("What is your name?: ")
    return player_name


def game_loop():
    pass


if __name__ == '__main__':
    main()
