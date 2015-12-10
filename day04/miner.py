import sys
import md5

def mine(secret, zeroes=5):
    number = 1
    while True:
        possible_match = '%s%s' % (secret, number)
        if md5.new(possible_match).hexdigest()[:zeroes] == '0' * zeroes:
            return number
        number += 1


if __name__ == '__main__':
    secret_key = sys.argv[1]
    zeroes = int(sys.argv[2])
    print(mine(secret_key, zeroes=zeroes))
