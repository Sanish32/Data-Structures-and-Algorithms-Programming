"""
Your task is to design a class that supports adding an edge to a directed graph and finding if the graph contains a directed cycle.

You may assume that the number of vertices is at most 50 and that the methods of the class are called at most 100 times.
"""

class Cycles:
    def __init__(self,n):
        # TODO
        self.n=n
        self.adjacencylist=[[] for _ in range(n+1)]
        self.color=["white"]*(n+1)
 
    def add_edge(self,a,b):
        # TODO
        self.adjacencylist[a].append(b)
 
    def DFS(self,u):
        self.color[u]="gray"
        for v in self.adjacencylist[u]:
            if self.color[v]=="gray":
                self.checker=True
                return
            elif self.color[v]=="white":
                self.DFS(v)
                
            if self.checker==True:
                return 
        
        self.color[u]="black"
 
    def check(self):
        # TODO
        self.color=["white"]*(self.n+1)
        
        self.checker=False
        for v in range(len(self.color)):
            if v==0:
                continue
            
            if self.color[v]=="white":
                self.DFS(v)
                if self.checker==True:
                    break
 
        return self.checker
        
if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True