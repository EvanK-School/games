#!/usr/bin/env python

import random as rd
import time as tm
import os
from sys import argv, exit

# Clearing, Welcome screen
if '-c' in argv: print(os.popen('clear').read()); argv.remove('-c')

print('Welcome to Mastermind!')
print('See README.md for help')
tm.sleep(0.5)
print('Generating random 4-digit number...')
print()
tm.sleep(1.5)

# Determining difficulty
my_max = 9
if len(argv) > 1:
    if argv[1] == '-d' and argv[2][0].isdigit():
        my_max = int(argv[2][0])

print('Based on your difficulty, there are {0} possible combinations'.format((my_max + 1) ** 4))

# Setup
num = []
for x in range(4):
    num.append(str(rd.randint(0, my_max)))

# Game Loop
count = 0
while True:
    count += 1
    correct = 0
    guess = input('> ')
    if len(guess) == 4 and guess.isdigit():
        lst = list(guess)
        for x in range(4):
            if lst[x] == num[x]:
                correct += 1

        print('*' * correct)

        if correct == 4:
            break
    elif guess.lower() == 'exit':
        exit()
    else:
        count -= 1

# Ending the Game
tries = '{0} tries'.format(count)
nice = ['Nice! ', 'Well done! ', 'Good Job! ', 'Impressive! ']
tote = ['All in all, you took: ', 'That took you: ', 'In the end, that was: ']
print(rd.choice(nice) + rd.choice(tote) + tries + '.')
print()
