import sys


def delivery(directions, santas=1):
    
    houses = {}

    positions = [(0, 0)] * santas
    
    actions = {
        '<': lambda x: (x[0] - 1, x[1]),
        '^': lambda x: (x[0], x[1] - 1),
        '>': lambda x: (x[0] + 1, x[1]),
        'v': lambda x: (x[0], x[1] + 1)
    }

    houses[positions[0]] = 1

    for idx, direction in enumerate(directions):
        position = positions[idx % santas]
        new_position = actions.get(direction)(position)
        houses[new_position] = 1
        positions[idx % santas] = new_position
    
    return len(houses)

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    directions = input_file.readline().strip()
    print(delivery(directions, int(sys.argv[2])))
