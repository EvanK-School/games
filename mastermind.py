#!/usr/bin/env python

import random as rd
import time as tm
import os
from sys import argv

print(os.popen('clear').read())

print('Welcome to Mastermind!')
print('See README.md for help')
tm.sleep(0.5)
print('Generating random 4-digit number...')
tm.sleep(1.5)

maxi = 9
if len(argv) > 1:
    if argv[1] == '-d' and argv[2][0].isdigit():
        maxi = int(argv[2][0])

print('Based on your difficulty, there are {0} possible combinations'.format((maxi + 1) ** 4))

num = []
for x in range(4):
    num.append(str(rd.randint(0, maxi)))

count = 0

while True:
    count += 1
    correct = 0
    lst = list(input('> '))
    for x in range(4):
        if lst[x] == num[x]:
            correct += 1

    print('*' * correct)

    if correct == 4:
        break

tries = '{0} tries'.format(count)
nice = ['Nice! ', 'Well done! ', 'Good Job! ', 'Impressive! ']
tote = ['All in all, you took: ', 'That took you: ', 'In the end, that was: ']
print(rd.choice(nice) + rd.choice(tote) + tries + '.')
print()
