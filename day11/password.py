import sys


def next_password(current_password):
    new_password = current_password

    while True:
        new_password = next_string(new_password)
        if check_password(new_password):
            break

    return new_password


def check_password(password):
    index = 0
    sequence_found = False
    letter_pairs = []
    while index <= len(password) - 2:
        char = password[index]
        if char in 'iol':
            return False

        if not sequence_found and password[index:3 + index] == char_sequence(char, 3):
            sequence_found = True

        if len(letter_pairs) < 2 and not char in letter_pairs: #Check for letter pairs
            if char == password[index + 1]:
                letter_pairs.append(char)

        index += 1

    return len(letter_pairs) == 2 and sequence_found


def char_sequence(char, size):
    count = 1
    string = char
    while count < size:
        char, rollover = next_char(char)
        if rollover:
            return None # Not a valid sequence
        string += char
        count += 1
    return string


def next_string(string):
    string = list(string)
    index = len(string) - 1
    while True:
        string[index], rollover = next_char(string[index])
        
        if not rollover:
            break

        if index == 0:
            string.append('a') # 'First char rolled over z to a, we need to append a new char'
            break
        
        index -= 1 # Current char rolled over from z to a, need to advance the previous char

    return ''.join(string)


def next_char(char):
    if char == 'z':
        return 'a', True
    return chr(ord(char) + 1), False


if __name__ == "__main__":
    password = sys.argv[1]
    print(next_password(password))
