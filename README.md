# tsp_evolution_algorithm

About:
This repo has source code for a heuristic method for solving Traveling Salesman Problem using the
application of evolution algorithm and nearest insertion algorithm.

Nearest algorithm is a Traveling Salesman Problem solving algorithm in which each node is selected,
then inserted into a currently formed cycle until there are no nodes left to be inserted.

First, three nodes, preferrably two closest node from an initially selected starting node, are formed
to form an initial cycle.

Second, a node (among pool of unselected nodes) that has the closest distance or smallest cost from
each one of the nodes in the cycle is selected. Among those selected nodes, node with the closest
distance or the smallest cost is selected again.

Lastly, the selected node is inserted into the cycle. This node is inserted between two consecutiv
nodes in the cycle in a way that the total cost or distance of the cycle is minimally increased. In
other words, two consecutive nodes are selected for the insertion with the cheapest cost.

Evolution algorithm is a type of heuristic in which a random mutation is occured among the population
better performance or certain value each generation.

To use evolution algorithm with nearest insertion, it is the best to first create an initial solution
with one iteration of nearest insertion. Then, for each generation, certain number of nodes is selected
and are removed, then inserted back again using nearest insertion. Also during this process, many
different groups of nodes are selected for randomness. During this mutation, the best path is selected,
and then the mutation is done again for the next generation. This whole process is repeated until
certain termination threshold.
