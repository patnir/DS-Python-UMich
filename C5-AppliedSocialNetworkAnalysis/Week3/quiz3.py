import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_nodes_from(["A", "B", "C", "D", "E", "F"])
list_edges = [["A","B"],["A","C"],["B","D"],["C","D"],["C","E"],["D","E"],["D","G"],["E","G"],["F","G"]]
g.add_edges_from(list_edges)

degCent = nx.degree_centrality(g)
print(degCent["D"])
closeCent = nx.closeness_centrality(g)
print(closeCent["G"])
print(closeCent)

betCent = nx.betweenness_centrality(g,normalized=True,weight=None,endpoints=False)
print(betCent["G"])
print(betCent)

edgeBetCent = nx.edge_betweenness_centrality(g, normalized=False)
print(edgeBetCent[('F', 'G')])


G = nx.DiGraph()
G.add_nodes_from(["A", "B", "C", "D"])
list_edges = [["A","B"], ["B","A"], ["A","C"], ["C","D"], ["D","C"]]
G.add_edges_from(list_edges)
nx.draw_networkx(G)
plt.show()

