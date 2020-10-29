from math import inf

from structure import RouteMap

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
            if neighbor in visited:
                continue
            if distance[neighbor] > distance[current] + weight[(current, neighbor)]:
                distance[neighbor] = distance[current] + weight[(current, neighbor)]
                parent[neighbor] = current
        visited.append(current)
    pa = parent[end]
    while pa != '':
        print(pa)
        pa = parent[pa]
    
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

    dijsktra(network, 'A', 'G')