import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Instantiate the graph
G1 = nx.Graph()
# add node/edge pairs
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (0, 5),
                   (1, 3),
                   (1, 6),
                   (3, 4),
                   (4, 5),
                   (4, 7),
                   (5, 8),
                   (8, 9)])

# draw the network G1
# nx.draw_networkx(G1)


# G=nx.MultiGraph()
# G.add_node('A',role='manager')
# G.add_edge('A','B',relation = 'friend')
# G.add_edge('A','C', relation = 'business partner')
# G.add_edge('A','B', relation = 'classmate')
# G.node['A']['role'] = 'team member'
# G.node['B']['role'] = 'engineer'
#
# print(G.nodes(data=True))

G = nx.MultiGraph()
G.add_node('A',role='manager')
G.add_edge('A','B',relation = 'friend')
G.add_edge('A','C', relation = 'business partner')
G.add_edge('A','B', relation = 'classmate')
G.node['A']['role'] = 'team member'
G.node['B']['role'] = 'engineer'


print(G.get_edge_data("A", "B", key={0, "relation"}))
