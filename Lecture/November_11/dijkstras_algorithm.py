"""
    Garfield Maitland
    CS 5001
    11/15/2023
    Practice - dijkstras_algorithm.py
"""
import heapq

graphs = {
    's': {'a': 8, 'b': 4},
    'a': {'b': 4},
    'b': {'a': 3, 'c': 2, 'd': 5},
    'c': {'d': 2},
    'd': {'a': 9, 'e': 3},
    'e': {'a': 2, 'b': 5, 'f': 50},
    'f': {'a': 90, 'g': 99},
    'g': {}
    # 'y': {'z': 20}
}


class Node:
    def __init__(self):
        self.d = float('inf')
        self.parent = None
        self.finished = False

    def __str__(self):
        return f"Distance: {self.d}, Parent: {self.parent}, Finished: {self.finished}"


def dijkstra(graph, source):
    nodes = {}
    for node in graph:
        nodes[node] = Node()
    nodes[source].d = 0
    queue = [(0, source)]  # priority queue
    while queue:
        d, node = heapq.heappop(queue)
        if nodes[node].finished:
            continue
        nodes[node].finished = True
        for neighbor in graph[node]:
            if nodes[neighbor].finished:
                continue
            new_d = d + graph[node][neighbor]
            if new_d < nodes[neighbor].d:
                nodes[neighbor].d = new_d
                nodes[neighbor].parent = node
                heapq.heappush(queue, (new_d, neighbor))
    for node in nodes:
        print(f"Node {node}: {nodes[node]}")
    return nodes


def main():
    dijkstra(graphs, 's')
    print("Graph Traversal Completed!")


if __name__ == "__main__":
    main()