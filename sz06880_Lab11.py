# Ex: 01
print("Ex:01 - Depth First Search :")
graph = { 0 : [2,1], 1 : [2,3], 2 : [4], 3 : [4,5], 4 : [5], 5 : []}
visited = set() 
def dfs(visited, graph, node):
    if node not in visited:
        print(node) 
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def main():
    dfs(visited, graph, 0)

if __name__ == "__main__":
    main()

# Ex : 02
def addEdges(G, edges_list, directed):
    if directed == False:
        for e, f, g in edges_list:
            G[e].append((f, g))
            G[f].append((e, g))
        return(G)
    else:
        for e, f, g in edges_list:
            G[e].append((f, g))        
        return G   

def Airport(aa, bb): 
    visited = [False]   
    queue = []  
    queue.append(bb) 
    visited[bb] = True
    while queue:  
        t = queue.pop(0) 
        if t == 0:
            print("s",end=" ")
        else:
            print (t, end = " ") 

# Ex: 03
from collections import defaultdict
graph = defaultdict(list)
graph[0].append(1)
graph[0].append(2)
graph[1].append(3)
graph[1].append(4)
graph[1].append(5)
graph[2].append(6)
graph[6].append(7)

def BFS(graph):
    print("Ex:03 - Breadth First Search :")
    Q = list()
    Q.append(0)
    while len(Q) != 0:
        a = len(Q)
        for o in range(a):
            wat = Q.pop(0)
            print(wat, sep = " ")
            for o in graph[wat]:
                Q.append(o)
BFS(graph)
    
# Ex:04a
def nodes_on_level(G, level):
    print("Ex:04 (a) - nodes on level no.",level,":")
    Q = []
    initial = 0
    Q.append(0)
    while len(Q) != 0:
        a = len(Q)
        for i in range(a):
            wat = Q.pop(0)
            if level == initial:
                print(wat, sep = " ")
            for i in G[wat]:
                Q.append(i)
        initial = initial + 1
        if initial > level:
            return
nodes_on_level(graph, 2)

# Ex : 04b
def get_node_level(G, node):
    Q = []
    initial = int(0)
    Q.append(0)
    while len(Q) != 0:
        a = len(Q)
        for i in range(a):
            wat = Q.pop(0)
            if node == wat:
                print("Ex:04 (b) - Level of node", node,":")
                print(initial)
                return
            for i in G[wat]:
                Q.append(i)
        initial = initial + 1
get_node_level(graph, 3)
    







