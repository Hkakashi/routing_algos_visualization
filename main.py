import matplotlib.pyplot as plt

from structure import RouteMap, Visualizer
from dijsktra import dijsktra

def main():
    # do testing
    network = RouteMap()
    print('Please add link to the diagram in the following format: node node weight\nExample: A B 4\nType "finish" if you have finished input')
    while True:
        line = input('Add> ').strip()
        if line == 'finish':
            break
        network.add_edge(*line.split(' '))
        plt.close('all')
        vis = Visualizer(network)
        vis.draw()

    start = input('Please select start node: ').strip()
    end = input('Please select end node: ').strip()

    print('Start solving using dijsktra...')
    shortest_path = dijsktra(network, start, end)
    vis.highlight_edge(*shortest_path)
    print("Finished!")
    input('Press Enter to exit.')

main()