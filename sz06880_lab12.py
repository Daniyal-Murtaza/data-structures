# Ex: 01
print("Exercise no.1:")
graph = {'A': ['B', 'E', 'C'], 
        'B': ['A', 'D', 'E'], 
        'C': ['A', 'F', 'G'], 
        'D': ['B', 'E'], 
        'E': ['A', 'B', 'D'], 
        'F': ['C'], 
        'G': ['C']}

def getShortestPath(graph, fromm, to): 
    a , q = [] , [fromm] 
    if fromm == to: 
        print("nodes are same!") 
        return 
    while len(q) != 0: 
        c = q.pop(0) 
        n = c[-1]  
        if n not in a: 
            neighs = graph[n]  
            for neigh in neighs: 
                d = [c]
                d.append(neigh) 
                q.append(d)  
                if neigh == to: 
                    print("Shortest Path:", *d) 
                    return
            a.append(n)  
    else:       
        print("No Path!") 
        return 
getShortestPath(graph, 'A', 'G') 


# EX: 02
print("Exercise no.2:")
graph = {'A': ['B', 'E', 'C'], 
            'B': ['A', 'D', 'E'], 
            'C': ['A', 'F', 'G'], 
            'D': ['B', 'E'], 
            'E': ['A', 'B', 'D'], 
            'F': ['C'], 
            'G': ['C']}  

def Mod_getShortestPath(graph, fromm, to): 
    a , q = [] , [fromm] 
    if fromm == to: 
        print("nodes are same!") 
        return 
    while len(q) != 0: 
        c = q.pop(0) 
        n = c[-1]  
        if n not in a: 
            neighs = graph[n]  
            for neigh in neighs: 
                d = [c]
                d.append(neigh) 
                q.append(d)  
                if neigh == to: 
                    print("Modified Shortest Path:", *d) 
                    return
            a.append(n)  
    else:       
        print("No Path!") 
        return 
Mod_getShortestPath(graph, 'A', 'B') 