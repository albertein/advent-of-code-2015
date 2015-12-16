import sys


def go_gadget_go(clues, sues):
    return [sue for sue in sues if was_it_sue_on_the_kitchen_with_the_knife(clues, sue)]


def was_it_sue_on_the_kitchen_with_the_knife(clues, sue):
    for stuff, stuff_count in sue.get('stuff').iteritems():
        clues_count = clues.get(stuff)
        if clues_count is not None and clues_count != stuff_count:
            return False
    return True


if __name__ == '__main__':
    data = open(sys.argv[1], 'r').readlines()
    sues = []
    for item in data:
        parts = item.strip().replace(',', '').replace(':', '').split()
        sues.append({
            'number': parts[1],
            'stuff': { parts[index]: int(parts[index + 1]) for index in xrange(2, len(parts), 2) }
        })

    clues = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    print(go_gadget_go(clues, sues))


