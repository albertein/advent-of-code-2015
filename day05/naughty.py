#!/usr/bin/python

import sys


def naughty(data):
    nice = 0
    naughty_combos = ['ab', 'cd', 'pq', 'xy']
    for string in data:
        if any([combo in string for combo in naughty_combos]):
            continue
        if len([char for char in string if char in 'aeiou']) < 3:
            continue
        for idx, char in enumerate(string):
            if idx == len(string) - 1:
                continue
            if char == string[idx + 1]: # Matchs x*x
                nice += 1
                break

    return nice
    

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    data = input_file.readlines()
    print(naughty(data))
