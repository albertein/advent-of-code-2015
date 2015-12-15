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


def maximize_cookiness_for_fat_people(ingredients):
    teaspoons = 100
    total_calories = 500
    ingredient_combinations = combinations(len(ingredients), teaspoons)
    scores = [get_mix_score(combination, ingredients, target_calories=total_calories) for combination in ingredient_combinations]
    return max(scores)


def get_mix_score(combination, ingredients, target_calories=0):
    ingredients_calories = [stat[-1] for stat in ingredients]
    total_calories = sum(calories * combination[index] for index, calories in enumerate(ingredients_calories))
    if total_calories != target_calories:
        return 0
    stats = [[stat * combination[index] for stat in ingredient[0:-1]] for index, ingredient in enumerate(ingredients)]
    stats = [sum(stat) for stat in zip(*stats)]
    return reduce(lambda x, y: x * y if y > 0 else 0, stats, 1)


if __name__ == '__main__':
    ingredients = []
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        ingredients.append([int(item) for item in re.findall(r'-?\d+', line)])
    print(maximize_cookiness_for_fat_people(ingredients))

