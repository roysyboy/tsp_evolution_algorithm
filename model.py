import networkx as nx

# Create Model

# weight calculator that returns uniform small deviation in values
def weight1(i, j, raw_index):
    index = int(raw_index / 2)
    if i > j:
        return (i - j) % index + 1
    elif i < j:
        return (i + j) % index + 1

# weight calculator that returns uniform big deviation in values
def weight2(i, j, raw_index):
    index = raw_index * 4
    if i > j:
        return (19 * i - 9 * j) % index + 1
    elif i < j:
        return (19 * i + 9 * j) % index + 1

# weight calculator that returns random big deviation in values
def weight3(i, j, raw_index):
    index = int(raw_index / 2)
    if i > j:
        return (i ** 3 - j) % index + 1
    elif i < j:
        return (i ** 2 + j ** 2) % index + 1

# weight calculator that returns random big deviation in values
def weight4(i, j, raw_index):
    index = raw_index * 4
    if i > j:
        return (i ** 3 - j) % index + 1
    elif i < j:
        return (i ** 2 + j ** 2) % index + 1

# creates graph model with nodes and edges connecting each pair of ndoes
def createRandomModel(num_of_nodes):
    weights = {}
    DG = nx.DiGraph()
    for i in range(num_of_nodes):
        weights[i] = {}
        for j in range(num_of_nodes):
            if i != j:
                DG.add_weighted_edges_from([(i, j, weight4(i, j, num_of_nodes))])
                weights[i][j] = DG[i][j]['weight']
    return DG, weights
