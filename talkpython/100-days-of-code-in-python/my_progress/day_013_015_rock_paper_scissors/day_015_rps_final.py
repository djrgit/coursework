#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from day_014_rps_classes import Player, Roll


roll_choices = ['Rock', 'Paper', 'Scissors']

key_beats_value_matrix = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}


def main():
    print_header()

    #rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    #game_loop(player1, player2, rolls)
    game_loop(player1, player2)


def print_header():
    print('-------------------------------------')
    print('       ROCK-PAPER-SCISSORS GAME')
    print('-------------------------------------')
    print()


def get_players_name():
    players_name = input("What is your name?: ")
    return players_name


def game_loop(p1, p2):

    count = 1
    score = {p1.name: 0, p2.name: 0}

    while count < 4:
        print()

        print(f"Roll number: {count}")

        p2_roll = Roll(p2)
        p2_rolled = p2_roll.get_roll()
        print(f"Player 2 rolls {p2_rolled}")

        p1_roll = Roll(p1)
        p1_rolled = p1_roll.get_roll()
        print(f"Player 1 rolls {p1_rolled}")

        outcome = p1_roll.can_defeat(p2_rolled)
        print()

        score[p1.name] += outcome
        score[p2.name] += -1 * outcome
        print(f"Current Score: {score}")

        count += 1

    if score[p1.name] > score[p2.name]:
        print(f"{p1.name} wins!!!")
    elif score[p1.name] < score[p2.name]:
        print(f"{p2.name} wins...")
    elif score[p1.name] == score[p2.name]:
        print(f"The 3-round Rock-Paper-Scissors game was a DRAW - Repeat the game")
        main()


if __name__ == '__main__':
    main()
