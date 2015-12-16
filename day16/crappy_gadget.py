import sys


def go_gadget_go(clues, sues):
    return [sue for sue in sues if was_it_sue_on_the_kitchen_with_the_knife(clues, sue)]


def was_it_sue_on_the_kitchen_with_the_knife(clues, sue):
    for stuff, stuff_count in sue.get('stuff').iteritems():
        if not crappy_gadget_comparer(stuff, clues.get(stuff), stuff_count):
            return False
    return True


def crappy_gadget_comparer(stuff, clue_count, sue_count):
    if clue_count is None: # If the gadget missed a trace it doesn't mean it doesn't exists
        return True

    if stuff in ['cats', 'trees']:
        return sue_count > clue_count
    elif stuff in ['pomeranians', 'goldfish']:
        return sue_count < clue_count
    else:
        return sue_count == clue_count


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


