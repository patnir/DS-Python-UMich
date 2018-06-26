import networkx as nx
import pandas as pd
import numpy as np

def answer_one():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0)
    a = nx.from_pandas_edgelist(df, "#Sender", "Recipient")
    return a

def answer_two():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0)
    emails = len(df)
    name_set = set(df["#Sender"])
    name_set.update(list(df["Recipient"]))
    names = len(name_set)
    return names, emails
answer_two()


def answer_three():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0, dtype={"#Sender": "str", "Recipient": "str"})
    directed = nx.from_pandas_dataframe(df, "#Sender", "Recipient", create_using=nx.MultiDiGraph())
    return (len(sorted(nx.strongly_connected_components(directed))) == 1), nx.is_weakly_connected(directed)

answer_three()

def answer_three():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0, dtype={"#Sender": "str", "Recipient": "str"})
    directed = nx.from_pandas_dataframe(df, "#Sender", "Recipient", create_using=nx.MultiDiGraph())
    return (len(sorted(nx.strongly_connected_components(directed))) == 1), nx.is_weakly_connected(directed)


def answer_four():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0, dtype={"#Sender": "str", "Recipient": "str"})
    directed = nx.from_pandas_dataframe(df, "#Sender", "Recipient", create_using=nx.MultiDiGraph())
    comps = nx.weakly_connected_components(directed)
    return len(sorted(comps)[0])


def answer_four():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0, dtype={"#Sender": "str", "Recipient": "str"})
    directed = nx.from_pandas_dataframe(df, "#Sender", "Recipient", create_using=nx.MultiDiGraph())
    comps = nx.weakly_connected_components(directed)
    return len(sorted(comps)[0])


def answer_six():
    df = pd.read_csv("email_network.txt", delimiter="\t", header=0, dtype={"#Sender": "str", "Recipient": "str"})
    directed = nx.from_pandas_dataframe(df, "#Sender", "Recipient", create_using=nx.MultiDiGraph())
    lengths = np.array([[y, len(y.nodes())] for y in nx.strongly_connected_component_subgraphs(directed)])
    return lengths[np.argmax(lengths[:, 1])][0]


def answer_seven():
    G_sc = answer_six()
    return nx.average_shortest_path_length(G_sc)


def answer_eight():
    G_sc = answer_six()
    return nx.diameter(G_sc)


def answer_nine():
    G_sc = answer_six()
    diameter = nx.diameter(G_sc)
    eccen = nx.eccentricity(G_sc)
    e_list = set([e for e in eccen.keys() if eccen[e] == diameter])
    return e_list

def answer_ten():
    G_sc = answer_six()
    diameter = nx.radius(G_sc)
    eccen = nx.eccentricity(G_sc)
    e_list = set([e for e in eccen.keys() if eccen[e] == diameter])
    return e_list



def answer_thirteen():
    G = answer_six()
    undir_subgraph = G.to_undirected()
    G_un = nx.Graph(undir_subgraph)
    return G_un


def answer_fourteen():
    G = answer_thirteen()
    return nx.transitivity(G), nx.average_clustering(G)



answer_ten()