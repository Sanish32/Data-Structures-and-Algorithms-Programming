"""
A grid has nxn squares, which are all walls initially. 

The rows and columns are numbered 1…n. 

The walls are then gradually removed by converting them to floors.

Your task is to keep track of the number of rooms during the process. 

A room consists of a vertically or horizontally connected floor squares, as in earlier problems.

You may assume that n is at most 100 and that the methods of the class are called at most 10000 times. 

The wall squares at the edges of the grid are never removed.
"""

class WallGrid:
    def __init__(self,n):
        # TODO
        self.n=n
        self.counting=0
        self.just={}
        self.size={}
 
    def remove(self,x,y):
        # TODO
        if (x,y) not in self.just:
            self.just[(x,y)]=(x,y)
            self.size[(x,y)]=1
            self.counting+=1
        
        if (x,y+1) in self.just:
            if self.find((x,y))!=self.find((x,y+1)):
                self.counting-=1
                self.union((x,y),(x,y+1))
        
        if (x,y-1) in self.just:
            if self.find((x,y))!=self.find((x,y-1)):
                self.counting-=1
                self.union((x,y),(x,y-1))
 
        if (x+1,y) in self.just:
            if self.find((x,y))!=self.find((x+1,y)):
                self.counting-=1
                self.union((x,y),(x+1,y))
        
        if (x-1,y) in self.just:
            if self.find((x,y))!=self.find((x-1,y)):
                self.counting-=1
                self.union((x,y),(x-1,y))
 
    def find(self, x):
        while self.just[x]!=x:
            x=self.just[x]
        return x
 
    def union(self, x, y):
        x=self.find(x)
        y=self.find(y)
        if self.size[x]<self.size[y]:
            temp=x
            x=y
            y=temp
        self.just[y]=x
        self.size[x]+=self.size[y]
        
    
    def count(self):
        # TODO
        return self.counting
        
 
if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2,2)
    w.remove(4,2)
    print(w.count()) # 2
    w.remove(3,2)
    print(w.count()) # 1
    w.remove(2,4)
    w.remove(2,4)
    w.remove(4,4)
    print(w.count()) # 3
    w.remove(3,3)
    print(w.count()) # 3
    w.remove(3,4)
    print(w.count()) # 1