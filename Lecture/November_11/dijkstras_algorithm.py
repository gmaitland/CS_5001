"""
    Garfield Maitland
    CS 5001
    11/15/2023
    Practice - dijkstras_algorithm.py
"""

graphs = {
    's':{'a':8, 'b':4},
    'a':{'b':4},
    'b':{'a':3,'c':2, 'd':5},
    'c':{'d':2},
    'd':{}
}


class Node:
    def __init__(self, x_cord, y_coord):
        self.d = float('inf')
        self.parent = None
        self.finished = False


def dijkstra(graph, source):
    nodes={}
    for node in graph:
        nodes[node]=Node()
    nodes[source].d=0
    queue=[(0, source)] # priority queue
    while queue:
        d,node=heapq.heappop(queue)
        if noges[node].finished:
            continue
        nodes[node].finished=True
        for neighbor in graph[node]:
            if nodes[neighbor].finished:
                continue
        new_d=d+graph[node][neighbor]
        if new_d<nodes[neighbor].d:
            nodes[neighbor].d = new_d
            nodes[neighbor].parent = node
            heapq.heappush(queue,(new_d, neighbor))
    print(nodes)
    return nodes


def main():
    a = []
    b = {}
    dijkstra(graphs, a)


if __name__ == "__main__":
    main()
