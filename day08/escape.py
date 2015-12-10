import sys
import re


def count(lines):
    total = 0
    in_memory = 0
    encoded = 0
    for line in lines:
        re.match(r'[\"\\]', line)
        line = line.strip()
        total += len(line)
        encoded += len(line) + len(re.findall(r'([\"\\])', line)) + 2
        line = line[1:-1]
        index = 0
        while True:
            in_memory += 1
            if line[index] == '\\':
                if line[index + 1] == 'x': # Hex char 
                    index += 3 # Skip over escaped hex char
                else:
                    index += 1
            index += 1

            if index >= len(line):
                break

    return (total - in_memory, encoded - total)


if __name__ == "__main__":

    input_file = open(sys.argv[1])
    lines = input_file.readlines()
    print(count(lines))
