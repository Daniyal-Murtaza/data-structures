G = {
    0: [1],
    1: [0],
    2: [],
    3: []
}

def DFS(G,node,visit=[]):
    visit.append(node)
    for edge in G[node]:
        if edge not in visit:
            DFS(G,edge,visit)
    return visit

def BFS(G,node):
    from queue import Queue
    queue = Queue()
    queue.put(node)
    visited = []
    while not queue.empty():
        vertex = queue.get()
        visited.append(vertex)
        for i in G[vertex]:
            if i not in visited:
                queue.put(i)
    return visited
    
def friendcircles(G):
    lst = []
    for node in G.keys():
        a = BFS(G,node)
        a = sorted(a)
        if a in lst:
            pass
        else:
            lst.append(a)
    return lst
print(friendcircles(G))
            

    