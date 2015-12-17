import sys


def store_booze(containers, amount=0):
    if not amount:
        return

    container = containers[0]
    remaining_containers = containers[1:]

    amount_using_current_container = amount - container
    
    if amount_using_current_container == 0:
        yield (container,)

    if remaining_containers:
        for option in store_booze(remaining_containers, amount): # Combinations skipping current container
            yield option

        for option in store_booze(remaining_containers, amount_using_current_container): # Combinations using current container
            yield (container,) + option


def minimum_containers(options):
    minimum_containers = sys.maxint
    minumum_containers_options = []
    for option in options:
        if len(option) == minimum_containers:
            minumum_containers_options.append(option)
        elif len(option) < minimum_containers:
            minimum_containers = len(option)
            minumum_containers_options = [option]

    return minumum_containers_options


if __name__ == "__main__":
    containers = [int(container) for container in open(sys.argv[1], 'r')]
    options = list(store_booze(containers, amount=int(sys.argv[2])))
    print(len(options))
    print(len(minimum_containers(options)))

