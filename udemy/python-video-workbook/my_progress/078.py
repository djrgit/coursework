# Exercise 78 - Password Generator
import random

chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
random_pw = ''.join(random.sample(chars, 6))
print(random_pw)