
# A* search
# 3 input parametrar
from os import PathLike, pathsep
import csv
from tkinter import W

csv_file_name = open('100 nodes.csv')
csv_reader = csv.reader(csv_file_name, delimiter=',')


def f(g, h, n, w):
    return w*g[n] + h[n]*(1-w)

def update(to_äe, to_add, n):
    to_remove.remove(n)
    to_add.append(n)
    return 

def heuristic_function(csv_reader): # kolla med alla noder, om 0 ska det vara 0, om >0 räkna med x och y



    
    return 
def expand_graph_search(path_cost, node, frontier_list, reached_list, path_len, parent_nodes):
    for index in range(0, len(path_cost)): #Expand graph search, node is expanded -> creates a list of candidate child nodes
        weight = path_cost[index]

        if weight > 0:
            if (index not in frontier_list) and (index not in reached_list):
                frontier_list.append(index)
                parent_nodes[index] = node
                path_len[index] = path_len[node] + weight

            else:
                if path_len[index] > path_len[node] + weight:
                    path_len[index] = path_len[node] + weight
                    parent_nodes[index] = node

                    if index in reached_list:
                        update(reached_list, frontier_list, index)

    update(frontier_list, reached_list, node)
    return path_len, parent_nodes

def w_a_star_search(cost, heuristic, start, end, w):
    pathSet = []    

    frontier_list = [start] #node is added to the end of frontier
    reached_list = []

    path_len = {}
    path_len[start] = 0

    parent_nodes = {}
    parent_nodes[start] = start

    while len(frontier_list) > 0: # while frontier is not empty 
        node = None
        
        for n in frontier_list: # select best node
            if node == None or f(path_len, heuristic, n, w) < f(path_len, heuristic, node, w): 
                node = n

        if node == None:
            #No path exists
            print('No path exists')
            break

        if node in end: # stop if node state is the end state of the problem
            fv_n = f(path_len, heuristic, node, w)
            reconstruct = []

            temp = node

            while parent_nodes[temp] != temp: 
                reconstruct.append(temp)
                temp = parent_nodes[temp]

            reconstruct.append(temp)
            reconstruct.reverse()

            pathSet.append( (reconstruct, fv_n))
            update(frontier_list, reached_list, node)
            continue

        path_cost = cost[node] # detta ska nog räknas ut, kommer nog från filen

        
        
        path_len,parent_nodes = expand_graph_search(path_cost, node, frontier_list, reached_list, path_len, parent_nodes)
    
    # pathSet 
    if len(pathSet) > 0:
        pathSet = sorted(pathSet, key=lambda x: x[1])
        path = pathSet[0][0]
    else:
        path = []

    return path

give_cost = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,5,9,-1,6,-1,-1,-1,-1,-1],
    [0,-1,0,3,-1,-1,9,-1,-1,-1,-1],
    [0,-1,2,0,1,-1,-1,-1,-1,-1,-1],
    [0,6,-1,-1,0,-1,-1,5,7,-1,-1],
    [0,-1,-1,-1,2,0,-1,-1,-1,2,-1],
    [0,-1,-1,-1,-1,-1,0,-1,-1,-1,-1],
    [0,-1,-1,-1,-1,-1,-1,0,-1,-1,-1],
    [0,-1,-1,-1,-1,2,-1,0,0,-1,8],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,0,7],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0]
]
start = 1
give_goals = [6,7,10]
heuristic = [0,5,7,3,4,6,0,0,6,5,0]
w = 0.5
# Vi ska göra en heuristic funktion 

get_path = w_a_star_search(give_cost, heuristic, start, give_goals, w)
print(get_path)