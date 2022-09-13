
import csv

csv_file_name = open('100 nodes.csv')
csv_reader = csv.reader(csv_file_name, delimiter=',')

class  Node():
    def __init__(self, parent = None, position = None, index = None):
        self.parent = parent
        self.cost = 0  # detta är för att ta sig från parent till child, g är att ta sig från start till node

        self.positionx = position[0]
        self.positiony = position[1]
        self.index = index
        self.f = 0
        self.g = 0
        self.h = 0
    
        
def heuristic_function(node, end_node):
    h = abs(node.positionx - end_node.positionx) + abs(node.positiony - end_node.positiony)
    return h

def f(node, w):
    node.f = w*node.g+(1-w)*node.h
    return node.f
    
def select_best_node(frontier_list, w, end_node):
    fbest = None
    for current_node in frontier_list: 
        node = current_node
        h = heuristic_function(node, end_node)

        if fbest == None or f(node,w) < f(fbest, w):
            fbest = node
            i_best = current_node
        
        node = i_best
        frontier_list.remove(node)

    return node 

def expand_graph_search(node, nodes):
    child_list = []
    parent = node
    maze=nodes
    actions = {}
    counter=0
    for element in maze[node.index]:
        if element != 0 and counter>1:
            actions[counter-2]=element          #dictionary med state (dvs index) som key, och kostnad
        counter +=1
    print("ACTIONS: ", actions)


    for index, cost in actions.items(): #dvs 100 nodes typ 
        cords = get_coordinates(maze, index)
        child = Node(parent,cords, index)
        child.cost=cost
        child.g=parent.g+cost
        child_list.append(child) #hämta rätt node, från data? 
        
    return child_list



def a_star_search(nodes, start, end, weight):
    startcord = get_coordinates(nodes, start)
    endcord = get_coordinates(nodes,end)

    start_node = Node(None, startcord, start) # start är index, vi behöver x och y för denna node
    end_node = Node(None, endcord, end) # end är index, vi behöver x och y för denna node

    frontier_list = {}
    reached_list = {}

    frontier_list[start] =start_node
    reached_list[start] =start_node

    while len(frontier_list) > 0:
        node = select_best_node(frontier_list, weight, end_node)

        if end_node == node:
            return node

        child_list = expand_graph_search(node, nodes)
        print(child_list)

        for child in child_list: #göra en dubbel for-loop? Så att man går igenom reached
            if child.index in reached_list.keys():
                print("CHILD EXIST IN REACHED!!")
                

    return 

def get_nodes():
    maze = []
    count = 0

    for row in csv_reader:
        int_row=[]
        if count != 0: 
            for element in row:
                int_element = int(element)
                int_row.append(int_element)
        count += 1
        maze.append(int_row[1:])       
    maze.remove(maze[0])
    return maze

def choose_input():
    start_index = input('Choose a start index: ')
    end_index = input('Choose a end index: ')
    weight = input('Choose a weight: ')
    return int(start_index), int(end_index), float(weight)

def get_coordinates(nodes, index):
    cord = []
    node = nodes[index]
    cord.append(node[0])
    cord.append(node[1])
    return cord

def main():
    start_index, end_index, weight= choose_input()
    nodes = get_nodes()
    a_star_search(nodes, start_index, end_index, weight)

main()