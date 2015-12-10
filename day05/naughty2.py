import sys


def naughty(data):
    nice = 0
    for string in data:
        string = string.strip()

        match_combo = False
        for idx, char in enumerate(string):
            if idx >= len(string) - 1:
                continue
            combo = string[idx:idx+2]
            before = string[0:idx]
            after = string[idx+2:]
            
            if combo in before or combo in after:
                match_combo = True
                break

        if not match_combo:
            continue

        for idx, char in enumerate(string):
            if idx >= len(string) - 2: # EOF
                continue
            if char == string[idx + 2]:
                nice += 1
                break

    return nice
    

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    data = input_file.readlines()
    print(naughty(data))
