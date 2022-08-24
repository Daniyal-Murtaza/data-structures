# Ex:02

print("Ex:02 answer:")
dictie = {}
G = {
        'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'E': set([
            ('A', 'B', 5),
            ('A', 'E', 6),
            ('B', 'C', 6),
            ('A', 'D', 3),
            ('C', 'D', 10),
            ('D', 'F', 8),
            ('E', 'F', 9),
            ('F', 'G', 10),
            ('C', 'G', 2),
            ])
        }

def bbb(vert):
    if vert != dictie[vert]:
        dictie[vert] = bbb(dictie[vert])
    return (dictie[vert])

def ccc(x, y, kon):
    p , q = bbb(x) , bbb(y)
    if p != q:
        for k in kon:
            dictie[p] = q

def MSTkruskals(G):
    mst = set()
    for vert in G['V']:
        dictie[vert] = vert
    kon = list(G['E'])
    kon.sort()
    for k in kon:
        x, y, w = k
        if bbb(y) != bbb(x):
            mst.add(k)
            ccc(x, y, kon)
    return mst  
        
mst = MSTkruskals(G)

#-------------------------------------------------------------------------------------------------------------#

# Ex:03
print("Ex:03 answer:")

# using self and class approach to differentiate a little from previous method!
class graph:
    def __init__(self, vertices):
        self.V = vertices
        self.G = []

    def addedge(self, u, v, w):
        self.G.append([u, v, w])

    def search(self, p, i):
        if p[i] == i:
            return i
        return self.search(p, p[i])

    def kk(self, p, H, x, y):        
        mm , nn = self.search(p, x) , self.search(p, y)
        
        if H[mm] > H[nn]:
            p[nn] = mm
        elif H[mm] == H[nn]:
            p[nn] = mm
            H[mm] = H[mm] + 1
        else:
            p[mm] = nn

    def MST(self):
        ans = []
        i , e = 0 , 0
        self.G = sorted(self.G, key = lambda item: item[2])
        p , H = [] , []
        
        for node in range(self.V):
            p.append(node)
            H.append(0)
            
        while e < self.V - 1:
            u, v, w = self.G[i]
            i = i + 1
            x , y = self.search(p, u) , self.search(p, v)
            if x != y:
                e = e + 1
                ans.append([u, v, w])
                self.kk(p, H, x, y)
        mini = int(0)
        print("edges\t\tCost")
        
        for u, v, cost in ans:
            mini = mini + cost
            print(u+1," to ",v+1,"\t", (cost))
        
g = graph(8)
# converted into adjacency list!
g.addedge(0, 1, 240)
g.addedge(0, 2, 210)
g.addedge(0, 3, 340)
g.addedge(0, 4, 280)
g.addedge(0, 5, 200)
g.addedge(0, 6, 345)
g.addedge(0, 7, 120)

g.addedge(1, 2, 265)
g.addedge(1, 3, 175)
g.addedge(1, 4, 215)
g.addedge(1, 5, 180)
g.addedge(1, 6, 185)
g.addedge(1, 7, 155)

g.addedge(2, 3, 260)
g.addedge(2, 4, 115)
g.addedge(2, 5, 350)
g.addedge(2, 6, 435)
g.addedge(2, 7, 195)

g.addedge(3, 4, 160)
g.addedge(3, 5, 330)
g.addedge(3, 6, 295)
g.addedge(3, 7, 230)

g.addedge(4, 5, 360)
g.addedge(4, 6, 400)
g.addedge(4, 7, 170)

g.addedge(5, 6, 175)
g.addedge(5, 7, 205)

g.addedge(6, 7, 305)

#-------------------------------------------------------------#

# Ex:01
# print("Ex:01 answer:")
# dictie = {}
# G = {
# 'A': [('B', 5), ('E', 6), ('D', 3)],
# 'B': [('A', 5), ('C', 6)],
# 'C': [('B', 6), ('D', 10), ('G', 2)],
# 'D': [('A', 2), ('C', 10), ('F', 8)],
# 'E': [('A', 6), ('F', 9)],
# 'F': [('D', 8), ('E', 9), ('G', 10)],
# 'G': [('C', 2), ('F', 10)]
# }


# def MSTprims(G):
#     mst = set()
#     for vert in G['V']:
#         dictie[vert] = vert
#     kon = list(G['E'])
#     kon.sort()
#     for k in kon:
#         x, y, w = k
#         if bbb(y) != bbb(x):
#             mst.add(k)
#             ccc(x, y, kon)
#     return mst  
        
# mst = MSTprims(G)

#-----------------------------------------------------#
# Calling Function A/C to Exercises! 

# Ex:02
print(sorted(list(mst), key = lambda x:x[2]))

# Ex:03
print ("Minimum spanning tree")
g.MST()

# Ex:01
# print(sorted(list(mst), key = lambda x:x[2]))
#-----------------------------------------------------#
