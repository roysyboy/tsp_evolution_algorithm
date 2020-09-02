import networkx as nx

# weight calculator that returns random big deviation in values
def weight(i, j, raw_index):
    index = raw_index * 4
    if i > j:
        return (i ** 3 - j ** 2) % index + 1
    elif i < j:
        return (i ** 3 + j ** 2) % index + 1

# creates graph model with nodes and edges connecting each pair of nodes
# 이 function이 리턴하는 'weights'가 weight matrix입니다
def createRandomModel(num_of_nodes):
    weights = {}
    DG = nx.DiGraph()
    for i in range(num_of_nodes):
        weights[i] = {}
        for j in range(num_of_nodes):
            if i != j:
                DG.add_weighted_edges_from([(i, j, weight(i, j, num_of_nodes))])
                weights[i][j] = DG[i][j]['weight']
    return DG, weights
