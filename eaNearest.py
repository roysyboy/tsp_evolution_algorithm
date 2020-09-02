import random as rd
import networkx as nx
import sys
import time
import copy
import matplotlib.pyplot as plt
import math
from nearest_insertion import findNearestInsPath
from data_model import createRandomModel

## global variables

def evolNearest(numOfNodes, startNode, endNode):
    ## create model
    global og_weights, node_num
    DG, og_weights = createRandomModel(numOfNodes)
    weights = copy.deepcopy(og_weights) # copy of og_weights matrix
    unvisited = list(DG)
    # iterStepIndex = int(math.sqrt(numOfNodes) / 2) # steps skipped during mutation
    node_num = numOfNodes

    
    weight_mtx = []
    for i in range(node_num):
        weight_mtx.append([])
        for j in range(node_num):
            if i == j:
                weight_mtx[i].append(0)
            else:
                weight_mtx[i].append(og_weights[i][j])
        print(weight_mtx[i])

    # print(weight_mtx)

    ## remove start and end from unvisited list
    unvisited.remove(startNode)
    unvisited.remove(endNode)

    ## add start and end to current path
    path = []
    path.extend((startNode, endNode))

    ## find first path using nearest insertion
    path = findNearestInsPath(path, unvisited, og_weights, weights)
    
    ## reset weights matrix
    weights = copy.deepcopy(og_weights)

    start_time = time.time()
    ## find the best path using Evolution Algorithm
    bestPath, bestCost, costList = findEvolutionPath(path, weights, start_time)
    runtime = int(1000 * round((time.time() - start_time), 3))

    print('> evolution path: {}'.format(bestPath))
    print('> evolution cost: {}'.format(bestCost))
    print('--- runtime: {}ms ---'.format(runtime))

    plt.plot(costList)
    plt.ylabel('path cost')
    plt.show()

    return bestCost

## find the best path using Evolution Algorithm
def findEvolutionPath(path, weights, start_time):
    ## initialize pool variable
    global node_num, iterStepIndex
    bestPath = path
    bestCost = pathCost(bestPath)
    pathLen = node_num
    costList = [] ## keeps track of best cost of path

    ## set how many nodes to remove during each iteration
    nodeRemoveSize = node_num - 3
    # removeIndex = int(math.sqrt(node_num) / 2) ## how much to subtract from nodeRemoveSize
    iterStepIndex = 1 # steps skipped during mutation
    removeIndex = 1 ## how much to subtract from nodeRemoveSize

    ## iterate until nodeRemoveSize becomes zero
    while nodeRemoveSize > 0:
        # print('{}...'.format(i))
        curBestPath = generatePathPool(bestPath, bestCost, pathLen, nodeRemoveSize, weights)
        curCost = pathCost(curBestPath)

        ## check if bestCost & bestPath can be replaced
        if curCost < bestCost:
                bestCost = curCost
                bestPath = curBestPath

        ## change nodeRemoveSize
        nodeRemoveSize -= removeIndex
    
        costList.append(bestCost)
        
    return bestPath, bestCost, costList

## generate many paths and return the best one
def generatePathPool(bestPath, bestCost, pathLen, nodeRemoveSize, weights):
    global iterStepIndex
    curBest = bestPath
    ## set MAX value for nodeRemoveSize
    if nodeRemoveSize > pathLen - 2:
        nodeRemoveSize = pathLen - 2
    
    ## remove nodes from path randomly
    for i in range(1, pathLen - nodeRemoveSize - 1, iterStepIndex):
        path = mutation(bestPath, nodeRemoveSize, i, weights)
        ## replace with best
        curCost = pathCost(path)
        if curCost < bestCost:
            curBest = path
            bestCost = curCost

    return curBest

## mutate given path
def mutation(path, nodeRemoveSize, index, weights):
    newPath = path[:index]
    newPath.extend(path[index + nodeRemoveSize:])

    unvisited = path[index:index + nodeRemoveSize]
    weights = copy.deepcopy(og_weights)

    finishedPath = findNearestInsPath(newPath, unvisited, og_weights, weights)
    
    return finishedPath

## calculate cost of the given path
def pathCost(path):
    total = 0
    for i in range(len(path) - 1):
        total += og_weights[path[i]][path[i + 1]]
    return total

evolNearest(20, 1, 6)

