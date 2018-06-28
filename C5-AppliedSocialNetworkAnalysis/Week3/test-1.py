import networkx as nx
import pandas as pd
import numpy as np

G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)
degCent = nx.degree_centrality(G)
print(degCent[34])

closeCent = nx.closeness_centrality(G)
print(closeCent)