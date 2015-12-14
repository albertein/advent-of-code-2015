import sys


def race(descriptions, seconds=0):
    deers = []
    for item in descriptions:
        parts = item.strip().split()
        deers.append({'name': parts[0], 'speed': int(parts[3]), 'flying': int(parts[6]), 'resting': int(parts[-2])})

    max_distance = -sys.maxint
    for deer in deers:
        cycle_time = deer.get('flying') + deer.get('resting')
        cycles = seconds / cycle_time
        distance = cycles * (deer.get('speed') * deer.get('flying'))
        leftover = seconds - cycle_time * cycles
        if leftover > deer.get('flying'):
            distance += deer.get('flying') * deer.get('speed')
        else:
            distance += leftover * deer.get('speed')

        if distance > max_distance:
            max_distance = distance

    return max_distance

if __name__ == '__main__':
    descriptions = open(sys.argv[1], 'r').readlines()
    print(race(descriptions, seconds=int(sys.argv[2])))
