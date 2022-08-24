
G = {}
nodes = [0,1,2,3,4,5]
edges_list = [(0,1,1),(0,2,1),(1,2,1),(1,3,1),(2,4,1),(3,4,1),(3,5,1),(4,5,1)]
 
def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G

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

def listOfNodes(G):
    nodes = list(G.keys())
    return nodes            

def listOfEdges(G, directed):
    if directed == False:
        edges = list(G.values())
        return edges
    if directed == True:
        edges = list(G.values())
        return edges                   

def In_OutDegree(G):
    listie = list()
    for key in G.keys():                                         
        a = key                                                 
        for k in G[a]:
            listie.append(k)                                    
        (listie.count(4))
    for x in G.keys():
        count = int(0)
        for y in G[x]:
            listie.append((x,y))
            count = count + 1
(In_OutDegree(G))

def printDegree(G):                                               
    listie = [0] * len(G)                                         
    for e in range(len(G)):
        u = len(G[e])
        for f in range(u):
            z = G[e][f][1]      
            listie[e] += 1 * z
    for e in range(len(listie)):
        return
printDegree(G)

def getNeighbors(G, nodes):
	n = list()
	for t in G[nodes]:
		n.append(t[0])
	return n    

def getInNeighbors(G, node):
    inneigh=[]
    for d in G:
        if d !=node:
            for r in G[d]:
                if r[0]==node:
                    inneigh.append(d)
    return inneigh

def getOutNeighbors(G, node):
	on=[]
	for p in G[node]:
		on.append(p[0])
	return on
            
def isNeighbor(G, Node1, Node2):            
	for y in G[Node1]:
		if Node2 == y[0]:
			return (True)
	else:
		return (False)

def removeNodes(G, nodes):
    for node in nodes:
            G.pop(node)
            for i in G:
                for j in G[i]:
                    if j[0] == node:
                        G[i].pop(G[i].index(j))
    return G
                         
def displayGraph(G):
	print("Graph: ",G)
(displayGraph(G)) 
       
def display_adj_matrix(G):
	adj_matrix = []
	for i in G:
		adj_matrix.append([0]*len(G))
	for i in G:
		for j in G[i]:
			adj_matrix[i][j[0]] = j[1]
	print("adj matrix:" ,adj_matrix)
(display_adj_matrix(G))
    
    
    
    
    
    
    
    