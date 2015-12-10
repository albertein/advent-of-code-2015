import sys


def looknsay(string, iterations):

    count = 1
    digit = string[0]
    index = 0
    output = ''

    while True:
        index += 1
        if index == len(string):
            break
        if string[index] == digit:
            count += 1
        else:
            output += '%s%s' % (count, digit)
            digit = string[index]
            count = 1

    output += '%s%s' % (count, digit)

    iterations -= 1

    if iterations > 0:
        output = looknsay(output, iterations)

    return output


if __name__ == "__main__":
    print(len(looknsay(sys.argv[1], int(sys.argv[2]))))
