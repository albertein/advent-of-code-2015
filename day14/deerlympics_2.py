import sys


def race(descriptions, seconds=0):
    deers = []

    def is_flying(deer, second):
        cycle = deer.get('flying') + deer.get('resting')
        second = second % cycle
        return second > 0 and second <= deer.get('flying')

    for item in descriptions:
        parts = item.strip().split()
        deers.append({'name': parts[0], 'speed': int(parts[3]), 'flying': int(parts[6]), 'resting': int(parts[-2]), 'points': 0, 'distance': 0})

    for second in range(1, seconds + 1):
        for deer in deers:
            if is_flying(deer, second):
                deer['distance'] += deer.get('speed')

        max_distance = max(deers, key=lambda deer: deer.get('distance')).get('distance')
        for deer in deers:
            if deer.get('distance') == max_distance:
                deer['points'] += 1

    return max(deers, key=lambda deer: deer.get('points'))


if __name__ == '__main__':
    descriptions = open(sys.argv[1], 'r').readlines()
    print(race(descriptions, seconds=int(sys.argv[2])))
