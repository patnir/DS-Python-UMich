import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])

# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])


# you can use the following function to plot graphs
# make sure to comment it out before submitting to the autograder
def plot_graph(G, weight_name=None):


    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None

    if weight_name:
        weights = [int(G[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(G, weight_name)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights)
    else:
        nx.draw_networkx(G, pos, edges=edges)
    plt.show()


def answer_one():
    # Your Code Here
    G_df = pd.read_csv('Employee_Movie_Choices.txt', delimiter="\t", header=0)
    G5 = nx.from_pandas_edgelist(G_df, '#Employee', 'Movie')
    print(G5.edges(data=True))
    nx.draw_networkx(G5)
    plt.show()
    return  # Your Answer Here


def answer_two():
    df = pd.read_csv('Employee_Movie_Choices.txt', delimiter="\t", header=0)
    asdf = answer_one()
    for node in asdf.nodes():
        print(node in df["#Employee"])
        print(node)
        if node in df["#Employee"]:
            asdf.node[node]["type"] = "employee"
        else:
            asdf.node[node]["type"] = "movie"
    return # Your Answer Here
answer_two()


def answer_four():
    df = pd.read_csv('Employee_Movie_Choices.txt', delimiter="\t", header=0)
    df2 = pd.read_csv('Employee_Relationships.txt', delimiter="\t", names=["n1", "n2", "weight"],
                      dtype={"n1": np.str, "n2": np.str, "weight": np.int})
    asdf = answer_two()

    X = set(list(df["#Employee"].astype("str")))
    P = bipartite.weighted_projected_graph(asdf, X)

    df2["scores"] = np.zeros(len(df2["weight"]))

    for edge in P.edges(data=True):
        df2.loc[((df2["n1"] == edge[0]) & (df2["n2"] == edge[1])) | (
        (df2["n2"] == edge[0]) & (df2["n1"] == edge[1])), "scores"] = edge[2]["weight"]

    return df2["weight"].corr(df2["scores"])

def answer_three():
    asdf = answer_two()
    df = pd.read_csv('Employee_Movie_Choices.txt', delimiter="\t", header=0)
    X = set(list(df["#Employee"].astype("str")))
    P = bipartite.weighted_projected_graph(asdf, X)
    return P
answer_three()

answer_four()

np.str

answer_one()
