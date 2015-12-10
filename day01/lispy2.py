import sys


def lispy(parens):
    
    actions = {
        '(': lambda x: x + 1,
        ')': lambda x: x - 1
    }

    floor = 0

    for index, paren in enumerate(parens):
        floor = actions.get(paren)(floor)
        if floor < 0:
            return index + 1


if __name__ == '__main__':
    print(lispy(sys.argv[1]))
