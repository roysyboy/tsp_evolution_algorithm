import random as rd
import networkx as nx
import sys
import copy
from model import createRandomModel

def nearestIns(numOfNodes, startNode, endNode):
    ## create model
    DG, og_weights = createRandomModel(numOfNodes)
    weights = copy.deepcopy(og_weights)
    unvisited = list(DG)

    ## remove start and end node since they are visited
    unvisited.remove(startNode)
    unvisited.remove(endNode)

    ## add start and end node to the path
    path = []
    path.extend((startNode, endNode))

    ## find path through farthest insertion
    path = findNearestInsPath(path, unvisited, og_weights, weights)

    ## calculate path cost
    totalCost = 0
    for i in range(len(path) - 1):
        totalCost += og_weights[path[i]][path[i + 1]]
    # print('> nearest insertion path = {}'.format(path))
    # print('> nearest insertion cost = {}'.format(totalCost))

    return totalCost

## find nearest node from current path
def findNearestInsPath(path, unvisited, og_weights, weights):
    while len(unvisited) > 0:
        ## selection from unvisited:
        new, unvisited, weights = nearestSelect(path, unvisited, weights)
        ## insertion to the path:
        path, unvisited, weights = cheapInsert(new, path, unvisited, og_weights, weights)
    return path

def nearestSelect(path, unvisited, weights):
    # print(' >>> path: {}'.format(path))
    bestVal = sys.maxsize
    new = None
    # print('len(path): {}'.format(len(path)))

    ## compare all insertions of unvisited node in all node pairs of the current path
    for i in range(len(path) - 1):
        thisNode = min(weights[path[i]], key=weights[path[i]].get)
        ## make sure the selected node hasn't been visited yet
        while thisNode in path:
            weights[path[i]].pop(thisNode)
            thisNode = min(weights[path[i]], key=weights[path[i]].get)
        thisVal = weights[path[i]][thisNode]
        if thisVal < bestVal:
            bestVal = thisVal
            new = thisNode
    # print('node selected: {}'.format(new))s
    unvisited.remove(new)

    return new, unvisited, weights

## insert the selected node in the current path in cheapest way possible
def cheapInsert(new, path, unvisited, og_weights, weights):
    smallestVal = sys.maxsize

    ## compare insertion of one of unvisited nodes between each node pair in current path
    for i in range(len(path) - 1):
        beforeThis, afterThis = path[i], path[i + 1]
        # print('beforeThis: {}, afterThis: {}'.format(beforeThis, afterThis))
        
        thisVal = og_weights[beforeThis][new] + og_weights[new][afterThis] - og_weights[beforeThis][afterThis]
        # print('selected node: {}'.format(thisNode))
        if thisVal < smallestVal:
            smallestVal = thisVal
            smallestIndex = i
    path.insert(smallestIndex + 1, new)

    ## remove the node from weights dict since it is about to be visited
    for node in unvisited:
        if new in weights[node].keys():
            weights[node].pop(new)
    
    return path, unvisited, weights


# nearestIns(10, 1, 6)