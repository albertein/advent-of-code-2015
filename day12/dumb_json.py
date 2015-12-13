import re
import sys


def dumb_parser(json):
    matches = re.findall(r'-?\d+', json)
    return sum([int(match) for match in matches])


if __name__ == "__main__":
    input_file = open(sys.argv[1], 'r')
    json = '\n'.join(input_file.readlines())
    print(dumb_parser(json))
