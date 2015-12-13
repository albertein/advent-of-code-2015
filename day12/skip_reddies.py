import sys
import json


def skip_reddies(data):
    total = 0
    if isinstance(data, list):
        for item in data:
            total += skip_reddies(item)
    elif isinstance(data, (int, long)):
        total = data
    elif isinstance(data, dict):
        for item in data.values():
            if item == 'red':
                total = 0
                break
            else:
                total += skip_reddies(item)

    return total


if __name__ == "__main__":
    input_file = open(sys.argv[1], 'r')
    json_text = '\n'.join(input_file.readlines())
    print(skip_reddies(json.loads(json_text)))
