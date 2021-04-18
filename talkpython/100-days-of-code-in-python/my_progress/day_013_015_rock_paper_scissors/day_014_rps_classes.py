#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


roll_choices = ['Rock', 'Paper', 'Scissors']

key_beats_value_matrix = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, Player):
        self.player = Player

    def get_roll(self, roll_list=roll_choices):
        self.roll = random.choice(roll_list)
        return self.roll

    def can_defeat(self, other_player_roll):
        if self.roll == other_player_roll:
            print(f"This roll was a DRAW")
            return 0   # Draw
        elif key_beats_value_matrix[self.roll] == other_player_roll:
            print(f"{self.player.name} wins this roll.")
            return 1   # Win
        else:
            print(f"The other player wins this roll.")
            return -1  # Loss

