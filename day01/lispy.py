import sys


def lispy(parens):
    return sum([1 if paren == '(' else -1 for paren in parens])


if __name__ == '__main__':
    print(lispy(sys.argv[1]))
