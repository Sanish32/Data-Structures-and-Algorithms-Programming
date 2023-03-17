"""
Bitland has n cities that initially have no connecting roads. 

The goal is to connect all cities to each other.

You are given a set of possible roads and the construction cost for each road. 

What is the smallest cost of a road network that connects all cities?

You may assume that the number of cities is at most 50 and that the methods of the class are called at most 100 times. 

The cost of each road is an integer in the range 1...1000.
"""

from heapq import heapify,heappop,heappush
class NewRoads:
    def __init__(self,n):
        # TODO
        self.n=n
        self.adjacencylist=[[] for _ in range(n+1)]
        self.inside=[]
 
 
    def add_road(self,a,b,x):
        # TODO
        self.adjacencylist[a].append((b,x))
        self.adjacencylist[b].append((a,x))
 
    def prim(self):
        f=[]
        self.inside=[False]*(self.n+1)
 
        self.inside[1]=True
 
        Q=[]
        heapify(Q)
 
        for item in self.adjacencylist[1]:
            heappush(Q,(item[1],1,item[0]))
        while Q:
            lightestedge=heappop(Q)
            u=lightestedge[2]
            
            if not self.inside[u]:
                f.append((lightestedge[1],u,lightestedge[0]))
                print(f)
                
                self.inside[u]=True
 
                for edge in self.adjacencylist[u]:
                    if not self.inside[edge[0]]:
                        heappush(Q,(edge[1],u,edge[0]))
 
        return f
                    
 
    def min_cost(self):
        # TODO
        cost=0
        x=self.prim()
        print(x)
 
        for i in range(1,self.n+1):
            if not self.inside[i]:
                return -1
 
        for item in x:
            cost+=item[2]
        return cost
 
 
 
if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7