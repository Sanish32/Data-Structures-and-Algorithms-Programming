"""
Your task is to design a class that supports adding an edge to an undirected graph 
and finding the longest path such that each vertex has a larger identifier than its predecessor on the path.

You may assume that the number of vertices is at most 50 and that the methods of the class are called at most 100 times.
"""

class LongPath:
    def __init__(self,n):
        # TODO
        self.n=n
        self.adjacencylist=[[] for _ in range(self.n+1)]
        self.length=[0 for _ in range(self.n+1)]
        self.checker=False
 
    def add_edge(self,a,b):
        # TODO
        self.checker=True
        if a>b:
            self.adjacencylist[a].append(b)
        else:
            self.adjacencylist[b].append(a)
        
       
 
    def calculate(self):
        # TODO
        if self.checker==False:
            return 0
            
        self.color=["white" for _ in range(self.n+1)]
 
        for v in range(1,self.n+1):
            if self.color[v]=="white":
                self.DFS(v)
                
        return max(self.length)
 
    def DFS(self,u):
        self.color[u]="gray"
        self.length[u]=0
        newlength=0
        for v in self.adjacencylist[u]:
            if self.color[v]=="gray":
                continue 
            elif self.color[v]=="white":
                self.DFS(v)
            
            newlength=self.length[v]+1
            if newlength>self.length[u]:
                self.length[u]=newlength
            
        self.color[u]="black"
 
 
if __name__ == "__main__":
    l = LongPath(5)
    print(l.calculate())
    l.add_edge(1,5)
    print(l.calculate())
    l.add_edge(3,2)
    l.add_edge(1,3)
    print(l.calculate())
    l.add_edge(3,5)
    l.add_edge(2,1)
    l.add_edge(3,5)
    l.add_edge(3,1)