import re
import sys


def combinations(items, total):
    if items == 1:
        yield (total, )
        return
    items -= 1
    for i in xrange(total + 1):
        for combination in combinations(items, total - i):
            yield (i,) + combination


def maximize_cookiness(ingredients):
    teaspoons = 100
    ingredient_combinations = combinations(len(ingredients), teaspoons)
    scores = [get_mix_score(combination, ingredients) for combination in ingredient_combinations]
    return max(scores)


def get_mix_score(combination, ingredients):

    stats = [[stat * combination[index] for stat in ingredient] for index, ingredient in enumerate(ingredients)]
    stats = [sum(stat) for stat in zip(*stats)]
    return reduce(lambda x, y: x * y if y > 0 else 0, stats, 1)


if __name__ == '__main__':
    ingredients = []
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        ingredients.append([int(item) for item in re.findall(r'-?\d+', line)[0:-1]])
    print(maximize_cookiness(ingredients))

