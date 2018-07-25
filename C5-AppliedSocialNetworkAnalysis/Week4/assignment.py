import networkx as nx
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

P1_Graphs = pickle.load(open('A4_graphs','rb'))
P1_Graphs


def print_attributes(current):
    print(current)
    print(nx.average_shortest_path_length(current))
    print(nx.average_clustering(current))
    return


def max_calc(G):
    degrees = G.degree()
    degree_values = sorted(set(degrees.values()))
    histogram = [list(degrees.values()).count(i)/float(nx.number_of_nodes( G)) for i in degree_values]
    return np.argmax(histogram)/ len(histogram)


def graph_identification():
    res = []
    for G in P1_Graphs:
        clus_coeff = nx.average_clustering(G)
        degree_hist = max_calc(G)
        if degree_hist == 0:
            res.append('PA')
        elif clus_coeff < 0.1:
            res.append('SW_H')
        else:
            res.append('SW_L')
    return res


G = nx.read_gpickle('email_prediction.txt')

print(nx.info(G))


degCent = nx.degree_centrality(G)
closeCent = nx.closeness_centrality(G)
betCent = nx.betweenness_centrality(G)
hits = nx.hits(G)
pageRank = nx.pagerank(G, alpha=0.85)


def train_test_data():
    test_nodes = []
    train_nodes = []
    train_data = np.empty((0, 9), float)
    test_data = np.empty((0, 8), float)
    columns = np.array(
        ["Node", "Degree", "DegreeCent", "CloseCent", "BetCent", "Hub", "Authority", "PageRank", "ManagementSalary"])
    for node in G.nodes():
        currMS = G.node[node]["ManagementSalary"]
        degree = G.degree()
        if currMS == 1 or currMS == 0:
            train_nodes.append(node)
            train_data = np.append(train_data, np.array([[node, degree[node], degCent[node], closeCent[node],
                                                          betCent[node], hits[0][node], hits[1][node], pageRank[node],
                                                          currMS]]), axis=0)
        else:
            test_nodes.append(node)
            test_data = np.append(test_data, np.array([[node, degree[node], degCent[node], closeCent[node],
                                                        betCent[node], hits[0][node], hits[1][node], pageRank[node]]]),
                                  axis=0)
    train = pd.DataFrame(train_data, columns=columns)
    test = pd.DataFrame(test_data, columns=columns[:-1])
    print(test.head())
    return train_data, test_data


def salary_predictions():
    train, test = train_test_data()
    return


salary_predictions()
