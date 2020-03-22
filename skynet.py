import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
graph = {}
exit_nodes=[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if graph.get(n1, None):
        graph[n1].append(n2)
    else:
        graph[n1] = [n2,]
    if graph.get(n2, None):
        graph[n2].append(n1)
    else:
        graph[n2] = [n1,]


for node in graph.keys():
    graph[node]=list(set(graph[node]))

for i in range(e):
    ei = int(input())  # the index of a gateway node
    exit_nodes.append(ei)

def get_closest_path(start, exit, graph, path_passed=0):
    # path_passed is full path with next node included
    path_passed += 1
    for node in graph[start]:
        if node in exit:
            return start, node, path_passed
    # remove path to not fall into infinite loop checking same paths
    graph2=graph.copy()
    graph2[start].remove(node)
    graph2[node].remove(start)
    #print('graph',graph, 'graph2 ',graph2)
    sub_paths = {}
    for node in graph[start]:
        resp = get_closest_path(node, exit, graph2, path_passed)
        if resp:
            first, second, path_length = resp
            sub_paths[path_length] = [first, second]
    shortests_path = min(sub_paths.keys())
    return sub_paths[shortests_path][0], sub_paths[shortests_path][1], shortests_path


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    #node_disconnected = disconnect_closest_gateway(graph=graph,exit_nodes=exit_nodes,skynet_agent=si)

    first, second, path_length = get_closest_path(si, exit_nodes, graph)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print("Debug messages...", file=sys.stderr)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(first, second)

def disconnect_closest_gateway(graph, exit_nodes, skynet_agent):
    paths={}
    for exit_node in exit_nodes:
        last_node, exit_node = get_closest_path(skynet_agent, exit_nodes, graph)
    return "{} {}".format(last_node, exit_node)


