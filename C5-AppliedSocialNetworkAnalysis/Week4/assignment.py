
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 4

# In[ ]:

import networkx as nx
import pandas as pd
import numpy as np
import pickle


# ---
# 
# ## Part 1 - Random Graph Identification
# 
# For the first part of this assignment you will analyze randomly generated graphs and determine which algorithm created them.

# In[ ]:

P1_Graphs = pickle.load(open('A4_graphs','rb'))
P1_Graphs


# <br>
# `P1_Graphs` is a list containing 5 networkx graphs. Each of these graphs were generated by one of three possible algorithms:
# * Preferential Attachment (`'PA'`)
# * Small World with low probability of rewiring (`'SW_L'`)
# * Small World with high probability of rewiring (`'SW_H'`)
# 
# Anaylze each of the 5 graphs and determine which of the three algorithms generated the graph.
# 
# *The `graph_identification` function should return a list of length 5 where each element in the list is either `'PA'`, `'SW_L'`, or `'SW_H'`.*

# In[ ]:

def print_attributes(current):
    print(current)
    print(nx.average_shortest_path_length(current))
    print(nx.average_clustering(current))
    return

def max_calc(G):
#     import matplotlib.pyplot as plt
#     print_attributes(G)
    degrees = G.degree()
    degree_values = sorted(set(degrees.values()))
    histogram = [list(degrees.values()).count(i)/float(nx.number_of_nodes( G)) for i in degree_values]
    return (np.argmax(histogram)/ len(histogram))

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


graph_identification()


# ---
# 
# ## Part 2 - Company Emails
# 
# For the second part of this assignment you will be workking with a company's email network where each node corresponds to a person at the company, and each edge indicates that at least one email has been sent between two people.
# 
# The network also contains the node attributes `Department` and `ManagementSalary`.
# 
# `Department` indicates the department in the company which the person belongs to, and `ManagementSalary` indicates whether that person is receiving a management position salary.

# In[ ]:

G = nx.read_gpickle('email_prediction.txt')

print(nx.info(G))


# ### Part 2A - Salary Prediction
# 
# Using network `G`, identify the people in the network with missing values for the node attribute `ManagementSalary` and predict whether or not these individuals are receiving a management position salary.
# 
# To accomplish this, you will need to create a matrix of node features using networkx, train a sklearn classifier on nodes that have `ManagementSalary` data, and predict a probability of the node receiving a management salary for nodes where `ManagementSalary` is missing.
# 
# 
# 
# Your predictions will need to be given as the probability that the corresponding employee is receiving a management position salary.
# 
# The evaluation metric for this assignment is the Area Under the ROC Curve (AUC).
# 
# Your grade will be based on the AUC score computed for your classifier. A model which with an AUC of 0.88 or higher will receive full points, and with an AUC of 0.82 or higher will pass (get 80% of the full points).
# 
# Using your trained classifier, return a series of length 252 with the data being the probability of receiving management salary, and the index being the node id.
# 
#     Example:
#     
#         1       1.0
#         2       0.0
#         5       0.8
#         8       1.0
#             ...
#         996     0.7
#         1000    0.5
#         1001    0.0
#         Length: 252, dtype: float64

# In[5]:

degCent = nx.degree_centrality(G)
closeCent = nx.closeness_centrality(G, normalized=True)
betCent = nx.betweenness_centrality(G, normalized=True)    
hits = nx.hits(G)
pageRank = nx.pagerank(G, alpha=0.85)
clustering = nx.clustering(G)


# In[31]:

from sklearn.metrics import recall_score, accuracy_score, precision_score
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import MinMaxScaler

def train_test_data():
    test_nodes = []
    train_nodes = []
    train_data = np.empty((0,10), float)
    test_data = np.empty((0,9), float)
    columns = np.array(["Node", "Degree", "DegreeCent", "Clustering", "CloseCent", "BetCent", "Hub", "Authority", "PageRank", "ManagementSalary"])
    for node in G.nodes():
        currMS = G.node[node]["ManagementSalary"]
        degree = G.degree()
        if currMS == 1 or currMS == 0: 
            train_nodes.append(node)
            train_data = np.append(train_data, np.array([[node, degree[node], degCent[node], clustering[node], closeCent[node], betCent[node], hits[0][node], hits[1][node], pageRank[node], currMS]]), axis=0)
        else: 
            test_nodes.append(node)
            test_data = np.append(test_data, np.array([[node, degree[node], degCent[node], clustering[node], closeCent[node], betCent[node], hits[0][node], hits[1][node], pageRank[node]]]), axis=0)
    train = pd.DataFrame(train_data, columns=columns)
    test = pd.DataFrame(test_data, columns=columns[:-1])
    return train, test
    
def print_stats(y_test, y_prediction):
    
#     print("accuracy  = {}".format(accuracy_score(y_test, y_prediction)))
#     print("recall    = {}".format(recall_score(y_test, y_prediction)))
#     print("precision = {}".format(precision_score(y_test, y_prediction)))
    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prediction)
    roc_auc_lr = auc(fpr_lr, tpr_lr)
    print("auc       = {}\n".format(roc_auc_lr))
    
def salary_predictions():
    train, test = train_test_data()
    train.index = train["Node"]
    test.index = test["Node"]
    train_nodes = train["Node"]
    test_nodes = test["Node"]
    train = train.drop(["Node", "Authority", "BetCent", "PageRank"], 1)
    test = test.drop(["Node", "Authority", "BetCent", "PageRank"], 1)

    X = train.iloc[:, :-1]
    y = train.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    test_scaled = scaler.transform(test)

    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)
    y_prediction = model.predict(X_test)

#     print_stats(y_test, y_prediction)

    predicted = model.predict(test)
    
    return pd.Series(index=test_nodes,data=predicted)

salary_predictions()


# ### Part 2B - New Connections Prediction
# 
# For the last part of this assignment, you will predict future connections between employees of the network. The future connections information has been loaded into the variable `future_connections`. The index is a tuple indicating a pair of nodes that currently do not have a connection, and the `Future Connection` column indicates if an edge between those two nodes will exist in the future, where a value of 1.0 indicates a future connection.

# In[116]:

future_connections = pd.read_csv('Future_Connections.csv', index_col=0, converters={0: eval})
future_connections.head(10)


# Using network `G` and `future_connections`, identify the edges in `future_connections` with missing values and predict whether or not these edges will have a future connection.
# 
# To accomplish this, you will need to create a matrix of features for the edges found in `future_connections` using networkx, train a sklearn classifier on those edges in `future_connections` that have `Future Connection` data, and predict a probability of the edge being a future connection for those edges in `future_connections` where `Future Connection` is missing.
# 
# 
# 
# Your predictions will need to be given as the probability of the corresponding edge being a future connection.
# 
# The evaluation metric for this assignment is the Area Under the ROC Curve (AUC).
# 
# Your grade will be based on the AUC score computed for your classifier. A model which with an AUC of 0.88 or higher will receive full points, and with an AUC of 0.82 or higher will pass (get 80% of the full points).
# 
# Using your trained classifier, return a series of length 122112 with the data being the probability of the edge being a future connection, and the index being the edge as represented by a tuple of nodes.
# 
#     Example:
#     
#         (107, 348)    0.35
#         (542, 751)    0.40
#         (20, 426)     0.55
#         (50, 989)     0.35
#                   ...
#         (939, 940)    0.15
#         (555, 905)    0.35
#         (75, 101)     0.65
#         Length: 122112, dtype: float64

# In[117]:

resource_allocation = list(nx.resource_allocation_index(G))
adamic_adar_index = nx.adamic_adar_index(G)
preferential_attachment = list(nx.preferential_attachment(G))
cn_soundarajan_hopcroft = nx.cn_soundarajan_hopcroft(G)


# In[ ]:

def train_test_data():
    train = future_connections[~pd.isnull(future_connections['Future Connection'])]
    test = future_connections[pd.isnull(future_connections['Future Connection'])]
    
    pa = pd.DataFrame(data=preferential_attachment)
    pa.index = [pa[0], pa[1]]
    pa = pa.drop([0, 1], 1)
#     for index, row in train.iterrows():
#         print("{} {} ".format(index, pa.loc[index[0], index[1]][2]))
        
    print([pa.loc[index[0], index[1]][2] for index, row in train.iterrows()])
    return

def new_connections_predictions():
    train_test_data()
    
    return # Your Answer Here

new_connections_predictions()


# In[ ]:



