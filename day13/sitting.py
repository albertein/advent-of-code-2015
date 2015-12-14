import sys
from itertools import permutations


def sitting(rules_description, add_host=False):

    rules = {}
    guests = set()

    def add_rule(subject, neighbord, happiness):
        rules['%s-%s' % (subject, neighbord)] = happiness

    def get_happiness(guest, adjacent):
        return rules['%s-%s' % (guest, adjacent)]

    def get_neighbords(index, sitting):
        return (sitting[(index - 1) % len(sitting)], sitting[(index + 1) % len(sitting)])

    for description in rules_description:
        parts = description.strip()[0:-1].split()
        subject = parts[0]
        guests.add(subject)
        neighbord = parts[-1]
        multiplier = 1 if parts[2] == 'gain' else -1
        happiness = int(parts[3]) * multiplier
        add_rule(subject, neighbord, happiness)

    if add_host:
        for guest in guests:
            add_rule('host', guest, 0)
            add_rule(guest, 'host', 0)

        guests.add('host')


    guests = list(guests)
    max_happiness = -sys.maxint
    for permutation in permutations(guests):
        happiness = 0
        for index, guest in enumerate(permutation):
            for neighbord in get_neighbords(index, permutation):
                happiness += get_happiness(guest, neighbord)
        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


if __name__ == '__main__':
    rules = open(sys.argv[1], 'r').readlines()
    print(sitting(rules, add_host=sys.argv[2] == 'yes'))
