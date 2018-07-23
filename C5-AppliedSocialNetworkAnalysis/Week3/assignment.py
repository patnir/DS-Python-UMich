import networkx as nx

G1 = nx.read_gml('friendships.gml')


def answer_one():
    degCent = nx.degree_centrality(G1)
    closeCent = nx.closeness_centrality(G1)
    betCent = nx.betweenness_centrality(G1)

    return degCent[100], closeCent[100], betCent[100]


def answer_two():
    import operator
    degCent = nx.degree_centrality(G1)
    return sorted(degCent.items(), key=operator.itemgetter(1), reverse=True)[0][0]


def answer_three():
    import operator
    closeCent = nx.closeness_centrality(G1)
    return sorted(closeCent.items(), key=operator.itemgetter(1), reverse=True)[0][0]


def answer_four():
    import operator
    betCent = nx.betweenness_centrality(G1)
    return sorted(betCent.items(), key=operator.itemgetter(1), reverse=True)[0][0]


G2 = nx.read_gml('blogs.gml')


