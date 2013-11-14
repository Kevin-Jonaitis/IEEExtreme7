import fileinput

class Graph(object):

##    class Node(object):
##        self.value = 0
##        self.count = 0
##        def __init__(self,value):
##            self.value = value
##            self.count = 0
            
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        
##    def add_edge(self, from_node, to_node, distance):
##        self._add_edge(from_node, to_node, distance)
##        self._add_edge(to_node, from_node, distance)
##        self.add_node(from_node)
##        self.add_node(to_node)
     
    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
        self.add_node(from_node)
        self.add_node(to_node)

def dfs(graph,start):
    all_nodes[int(start) - 1] = all_nodes[int(start) - 1] + 1
    node = graph.edges[str(start)][0]
    while(not(node is None)):
        all_nodes[int(node) - 1] = all_nodes[int(node) - 1] + 1
        try:
            node = graph.edges[str(node)][0]
        except KeyError:
            break;

def bfs(graph,start,end):
    list_of_paths = [] ##list of all
##    the possible paths
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0); #pop the top of the queue
        node = path[-1] #grab the latest node
        if node == end:
            list_of_paths.append(path)
        for adjacent in g.edges[node]:
            if (not (adjacent in path)):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    if (len(list_of_paths) == 0):
        print "No Route Available from F to " + end
    else:
        shortest = 9223372036854775807
        for path in list_of_paths:
            if len(path) < shortest:
                shortest = len(path)
        print "Total Routes: " + str(len(list_of_paths))
        print "Shortest Route Length: " + str(shortest)
        shortest_paths = []
        for path in list_of_paths:
            if len(path) == shortest:
                shortest_paths.append(path)
        shortest_paths.sort()
        route = shortest_paths[0]
        str_route = ""
        for item in route:
            str_route += item + ' '
        print("Shortest Route after Sorting of Routes of length " + str(len(route)) + ": " + str_route.strip())


g = Graph()
rg = Graph()


##test_file = open('test.txt')
num_of_lines = input()

nodes_with_stuff_pointing_to_them = [0]*num_of_lines
nodes_with_stuff_coming_out_of_them = [0]*num_of_lines
all_nodes = [0]*num_of_lines


for line in fileinput.input():
    from_node, to_node = line.strip().split(" ")
    g._add_edge(from_node, to_node, 1)
    rg._add_edge(to_node,from_node,1)
    nodes_with_stuff_pointing_to_them[int(to_node) - 1] = nodes_with_stuff_pointing_to_them[int(to_node) - 1] + 1
    nodes_with_stuff_coming_out_of_them[int(from_node)- 1] = nodes_with_stuff_coming_out_of_them[int(from_node) - 1] + 1


left_edge_nodes = []
right_edge_nodes = []
hashmap_nodes = {}
for index in range(0,len(nodes_with_stuff_pointing_to_them)):
    if (nodes_with_stuff_pointing_to_them[index] == 0):
       left_edge_nodes.append(index + 1)
       
for index in range(0,len(nodes_with_stuff_coming_out_of_them)):
    if (nodes_with_stuff_coming_out_of_them[index] == 0):
        right_edge_nodes.append(index + 1)

##print left_edge_nodes
##print right_edge_nodes
##
##print g.edges
##print g.nodes

for node in left_edge_nodes:
    dfs(g,node)

for node in right_edge_nodes:
    dfs(rg,node)

##for value in all_nodes:
##    print value

##for index in range(0,len(all_nodes)):
##    print "Index:" + str(index + 1) + " has value " + str(all_nodes[index])

largest_value = -1
largest_value_list = []
for index in range(0,len(all_nodes)):
    if (all_nodes[index] > largest_value):
        largest_value = all_nodes[index]
        largest_value_list = [index + 1]
    elif (all_nodes[index] == largest_value):
        largest_value_list.append(index + 1)

for element in largest_value_list:
    print str(element)

##g = Graph()
##end_node = raw_input().strip()
##for line in fileinput.input():
##    if line != "A A":
##        from_node, to_node = line.strip().split(" ")
##        g.add_edge(from_node, to_node, 1)

##bfs(g,'F',end_node)

