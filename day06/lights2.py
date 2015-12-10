#!/usr/bin/python

import sys


def lights(instructions):
    light_board = {}

    def on(cords):
        light_board[cords] = light_board.get(cords, 0) + 1

    def off(cords):
        light = light_board.pop(cords, 0)
        light -= 1
        if light > 0:
            light_board[cords] = light


    def toggle(cords):
        light_board[cords] = light_board.get(cords, 0) + 2


    actions = {
        'on': on,
        'off': off,
        'toggle': toggle
    }

    for instruction in instructions:
        [actions.get(instruction[0])(cord) for cord in range_generator(instruction[1], instruction[2])]

    return sum(light_board.values())

def range_generator(source, target):
    multiplier_x = 1
    multiplier_y = 1

    if source[0] > target[0]:
        multiplier_x = -1
    if source[1] > target[1]:
        multiplier_y = -1

    while True:
        original_y = source[1]
        while True:
            yield (source[0], source[1],)
            if source[1] == target[1]:
                break
            source[1] += 1 * multiplier_y

        source[1] = original_y
        if source[0] == target[0]:
            break


        source[0] += 1 * multiplier_x


def parse_instruction(string_instruction):
    section = string_instruction.split(' ')
    instruction_type = None
    source = None
    target = None
    if section[0] == 'turn':
        instruction_type = section[1]
        source = section[2]
        target = section[4]
    else:
        instruction_type = 'toggle'
        source = section[1]
        target = section[3]


    return (instruction_type, [int(x) for x in source.split(',')], [int(x) for x in target.split(',')],)
    

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    data = input_file.readlines()
    instructions = [parse_instruction(instruction.strip()) for instruction in data]

    print(lights(instructions))
