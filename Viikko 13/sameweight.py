"""
Your task is to determine whether every spanning tree of a given graph has the same weight.

You may assume that the number of cities is at most 50 and that the methods of the class are called at most 100 times. 

The weight of each edge is an integer in the range 1...1000.
"""

from heapq import heapify,heappop,heappush
from itertools import count
class SameWeight:
    def __init__(self,n):
        # TODO
        self.n=n
        self.adjacencylist1=[[] for _ in range(n+1)]
        self.adjacencylist2=[[] for _ in range(n+1)]
        self.inside=[]
        self.counter=0
        self.checker1=False
        self.checker2=False
 
 
    def add_edge(self,a,b,x):
        # TODO
        self.adjacencylist1[a].append((b,x))
        self.adjacencylist1[b].append((a,x))
 
        self.adjacencylist2[a].append((b,-x))
        self.adjacencylist2[b].append((a,-x))
 
    def prim(self):
        f1=[]
        self.checker1=False
        self.checker2=False
        self.counter=0
        self.inside=[False]*(self.n+1)
 
        self.inside[1]=True
 
        Q=[]
        heapify(Q)
 
        for item in self.adjacencylist1[1]:
            heappush(Q,(item[1],1,item[0]))
        while Q:
            lightestedge=heappop(Q)
            u=lightestedge[2]
            
            if not self.inside[u]:
                f1.append((lightestedge[1],u,lightestedge[0]))
                self.counter+=1
                
                self.inside[u]=True
 
                for edge in self.adjacencylist1[u]:
                    if not self.inside[edge[0]]:
                        heappush(Q,(edge[1],u,edge[0]))
        print(self.counter)
        if self.counter<self.n-1:
            self.checker1=True
 
        self.counter=0
        f2=[]
        self.inside=[False]*(self.n+1)
 
        self.inside[1]=True
        for item in self.adjacencylist2[1]:
            heappush(Q,(item[1],1,item[0]))
        while Q:
            lightestedge=heappop(Q)
            u=lightestedge[2]
            
            if not self.inside[u]:
                f2.append((lightestedge[1],u,lightestedge[0]))
                self.counter+=1
                
                self.inside[u]=True
 
                for edge in self.adjacencylist2[u]:
                    if not self.inside[edge[0]]:
                        heappush(Q,(edge[1],u,edge[0]))
        print(self.counter)
        if self.counter<self.n-1:
            self.checker2=True
        return (f1,f2)
 
    def check(self):
        # TODO
        z=self.min_max()
        print(z)
    
        if z==True:
            return z
 
        if self.checker1==True or self.checker2==True:
            return True
        return z
 
    def min_max(self):
        # TODO
        weight1=0
        weight2=0
        x,y=self.prim()
 
        for item in x:
            weight1+=item[2]
        
        for item in y:
            weight2+=item[2]
 
        if (-1)*weight2==weight1:
            return True
        return False
 
if __name__ == "__main__":
    #s = SameWeight(4)
    #s.add_edge(1,2,2)
    #s.add_edge(1,3,3)
    #print(s.check()) # True
    #s.add_edge(1,4,3)
    #print(s.check()) # True
    #s.add_edge(3,4,3)
    #print(s.check()) # True
    #s.add_edge(2,4,1)
    #print(s.check()) # False
    s = SameWeight(5)
    s.add_edge(1,2,1)
    s.add_edge(1,4,3)
    s.add_edge(2,4,5)
    s.add_edge(4,5,3)
    print(s.check())