from math import inf
import time

from structure import RouteMap, Visualizer

def dijsktra(network, start, end):
    '''
    finding the shortest route from start router to end router using dijsktra algo
    network: RouterMap
    start, end: str
    return: list
    '''
    graph, weight, N = network.graph, network.weight, len(network.graph)
    # keep track of the minimal distance from the start to each router
    # initialize them as infinity
    distance = {router:inf for router in graph.keys()}
    # set the distance from start router to itself as 0
    distance[start] = 0
    # record the last router in the route of each router (call it 'parent')
    parent = {router:'' for router in graph.keys()}
    # record the routers that we have visited
    visited = []
    while len(visited) < N:
        # find the unvisited router with smallest distance 
        current = choose_smallest(distance, visited)
        neighbors = graph[current]
        for neighbor in neighbors:
            # if that neighbor is visited, we cannot find a shorter route
            if neighbor in visited:
                continue
            # update the shortest distance and its parent node if we find a shorter route
            if distance[neighbor] > distance[current] + weight[(current, neighbor)]:
                distance[neighbor] = distance[current] + weight[(current, neighbor)]
                parent[neighbor] = current
        # mark current node as visited
        visited.append(current)
    # form the shortest route
    path = []
    current = end
    last = parent[current]
    while last != '':
        path.append((current, last))
        current = last
        last = parent[current]
    return path
    
def choose_smallest(distance, visited):
    '''
    find the unvisited router with smallest distance
    '''
    ret, dis = '', inf
    for key, val in distance.items():
        if key in visited:
            continue
        if val < dis:
            dis = val
            ret = key
    return ret

if __name__ == '__main__':
    # do testing
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
    shortest_path = dijsktra(network, 'A', 'G')
    vis.highlight_edge(*shortest_path)
    input('test> ')