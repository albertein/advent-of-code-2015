import sys


class Node(object):

    def __init__(self, name):
        self.name = name
        self.connections = []


    def connect(self, node, distance):
        self.connections.append({
            'to': node,
            'distance': distance
        })
        node.connections.append({
            'to': self,
            'distance': distance
        })


    def find_path_shortest_path(self, remaining_nodes):
        remaining_nodes = remaining_nodes[:] # Copy the list
        remaining_nodes.remove(self)
        min_distance = sys.maxint
        for connection in self.connections:
            next_node = connection.get('to')
            if next_node not in remaining_nodes:
                continue # Node already visited
            distance = connection.get('distance') + next_node.find_path_shortest_path(remaining_nodes)
            if distance < min_distance:
                min_distance = distance
        return min_distance if min_distance < sys.maxint else 0


    def find_path_longest_path(self, remaining_nodes):
        remaining_nodes = remaining_nodes[:] # Copy the list
        remaining_nodes.remove(self)
        max_distance = 0
        for connection in self.connections:
            next_node = connection.get('to')
            if next_node not in remaining_nodes:
                continue # Node already visited
            distance = connection.get('distance') + next_node.find_path_longest_path(remaining_nodes)
            if distance > max_distance:
                max_distance = distance
        return max_distance


def travel(routes):
    nodes = {}

    def get_node(name):
        node = nodes.get(name)
        if not node:
            node = Node(name)
            nodes[name] = node
        return node

    for route in routes:
        section = route.strip().split()
        from_node = get_node(section[0])
        to_node = get_node(section[2])
        from_node.connect(to_node, int(section[4]))


    min_distance = min([node.find_path_shortest_path(nodes.values()) for node in nodes.values()])
    max_distance = max([node.find_path_longest_path(nodes.values()) for node in nodes.values()])

    return (min_distance, max_distance)


if __name__ == "__main__":
    lines = open(sys.argv[1], 'r').readlines()
    print(travel(lines))
