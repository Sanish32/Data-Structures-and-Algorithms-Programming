"""
Bitland has n cities that initially have no connecting roads. 
 
Your task is to design a class that supports adding a road between two cities and querying if there is a route between two cities.

You may assume that the number of cities is at most 50 and that the methods of the class are called at most 100 times.
"""

class Cities:
    def __init__(self,n):
        self.n=n
        self.adjacencylists=[[] for _ in range(self.n+1)]
        self.visited=[False]*(n+1)
 
    def add_road(self,a,b):
        self.adjacencylists[a].append(b)
        self.adjacencylists[b].append(a)
 
    def has_route(self,a,b):
        # TODO
        for s in range(1,(self.n)+1):
            self.visited[s]=False
 
        self.DFS(a)
        if not self.visited[b]:
            return False
        return True
    
    def DFS(self,u):
        self.visited[u]=True
        for v in self.adjacencylists[u]:
            if not self.visited[v]:
                self.DFS(v)
 
if __name__ == "__main__":
    c = Cities(5)
    print(c.has_route(4,5))
    print(c.has_route(1,4))
    c.add_road(4,5)
    print(c.has_route(4,5))
    print(c.has_route(1,3))
    c.add_road(1,5)
    print(c.has_route(3,5))
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(2,3))