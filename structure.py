from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt

class RouteMap:
    def __init__(self):
        # this variable stores the relationship between routers
        # key: router:str
        # val: [neighbor1:str, neighbor2:str, ...]
        self.graph = defaultdict(list)
        # this variable stores the weight of each link
        # key: (router1:str, router2:str)
        # val: weight:int
        self.weight = {}
    
    def add_edge(self, router1, router2, weight):
        '''
        Add edge to the route map. If route doesn't exist, it will auto create it.
        router1, router2: str
        weight: int
        '''
        weight = int(weight)
        self.graph[router1].append(router2)
        self.graph[router2].append(router1)
        self.weight[(router1, router2)] = weight
        self.weight[(router2, router1)] = weight

    def __str__(self):
        res = str(dict(self.graph)) + '\n' + str(self.weight)
        return res

class Visualizer:
    def __init__(self, route_map):
        graph = route_map.graph
        weight = route_map.weight
        self.network = nx.Graph()
        for node in graph.keys():
            self.network.add_node(node)
            for neighbor in graph[node]:
                wei = weight[(node, neighbor)]
                self.network.add_edge(node, neighbor, weight=wei, color='grey')
    
    def draw(self):
        # draw the network
        fig, ax = plt.subplots()
        plt.ion()
        self.pos = nx.circular_layout(self.network)
        nx.draw(self.network, pos=self.pos, ax=ax, with_labels=True) # show node label
        labels = nx.get_edge_attributes(self.network,'weight')
        nx.draw_networkx_edge_labels(self.network, pos=self.pos, edge_labels=labels)
        plt.show()

    def highlight_edge(self, *args, color='r'):
        '''
        highlight edges in red
        args = [(router1, router2), (..., ...), ...]
        '''
        fig, ax = plt.subplots()
        nx.draw(self.network, pos=self.pos, ax=ax, with_labels=True) # show node label
        nx.draw_networkx_edges(self.network, self.pos, edgelist=args, edge_color=color, width=2)
        labels = nx.get_edge_attributes(self.network,'weight')
        nx.draw_networkx_edge_labels(self.network, pos=self.pos, edge_labels=labels)
        plt.show()

# do some test
if __name__ == '__main__':
    network = RouteMap()
    network.add_edge('A', 'B', 2)
    network.add_edge('A', 'C', 4)
    network.add_edge('A', 'D', 7)
    network.add_edge('A', 'F', 5)
    network.add_edge('B', 'E', 3)
    network.add_edge('B', 'D', 6)
    network.add_edge('B', 'G', 8)
    network.add_edge('C', 'F', 6)
    network.add_edge('D', 'F', 1)
    network.add_edge('D', 'G', 6)
    network.add_edge('E', 'G', 7)
    network.add_edge('F', 'G', 6)
    vis = Visualizer(network)
    vis.draw()
    vis.highlight_edge(('A', 'B'), ('A', 'C'))