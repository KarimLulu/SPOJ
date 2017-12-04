from collections import defaultdict
from heapq import *
import numpy as np
import math
from sys import stdout

class Graph(object):

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(dict)
        self.node_name_map = dict()

    def add_edge(self, source, destination, cost):
        self.add_node(source)
        self.add_node(destination)
        self.edges[source][destination] = cost
        #self.edges[destination][source] = cost

    def add_node(self, node):
        self.nodes.add(node)

    def add_node_name(self, node, name):
        self.node_name_map[name] = node

    def find_shortest_path(self, source, destination):
        source = self.node_name_map[source]
        dest = self.node_name_map[destination]
        visited = set()
        h = []
        heappush(h, (0, source))

        while h:
            cost, vertex = heappop(h)
            visited.add(vertex)
            if vertex==dest:
                return cost

            for v, c in self.edges[vertex].items():
                if v not in visited:
                    heappush(h, (cost+c, v))
        return math.inf

t = int(input())
for k in range(t):
    if k>0:
        sep = input()
    n = int(input()) # number of cities
    graph = Graph()
    for city in range(n):
        name = input()
        graph.add_node(city+1)
        graph.add_node_name(city+1, name)
        neighbours = int(input())
        for neighbour in range(neighbours):
            nr, cost = input().split()
            graph.add_edge(city+1, int(nr), int(cost))
    r = int(input())
    for path in range(r):
        source, dest = input().split()
        stdout.write(str(graph.find_shortest_path(source, dest))+'\n')
