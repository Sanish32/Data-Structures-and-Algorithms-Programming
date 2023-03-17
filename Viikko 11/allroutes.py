"""
Bitland has n cities that initially have no connecting roads. 

Your task is to design a class that supports adding a road between two cities and computing a distance table.

A distance table is an nxn table where the entry on a row a and a column b is the length on the shortest route between the cities a and b.

If there is no route, the entry is -1.

Here too all the roads go both directions and thus the order of the two cities makes no difference. 

There may be multiple roads between two cities.

You may assume that the number of cities is at most 50 and that the methods of the class are called at most 100 times. 

The length of each road is an integer in the range 1...1000.
"""

class AllRoutes:
    def __init__(self,n):
        # TODO
        self.n=n
        self.roads=[]
 
    def add_road(self,a,b,x):
        # TODO
        y=0
        z=0
        for road in self.roads:
            if (a,b)==road[0]:
                y+=1
                if road[1]>x:
                    self.roads.remove((road[0],road[1]))
                    self.roads.append(((a,b),x))
                    z+=1
        if z==0 and y==0:
            self.roads.append(((a,b),x))
        z=0
        y=0
        for road in self.roads:
            if (b,a)==road[0]:
                y+=1
                if road[1]>x:
                    self.roads.remove((road[0],road[1]))
                    self.roads.append(((b,a),x))
                    z+=1
        if z==0 and y==0:
            self.roads.append(((b,a),x))
 
 
    def get_table(self):
        # TODO
        D=[[] for _ in range(self.n)]
 
        for i in range(self.n):
            for j in range(self.n):
                if i==j:
                    D[i].append(0)
                else:
                    x=0
                    for road in self.roads:
                        if (i+1,j+1)==road[0]:
                            D[i].append(road[1])
                            x+=1
                            break
                    if x==0:
                        D[i].append(99999)
 
 
        print(D)
 
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    D[i][j]=min(D[i][j],D[i][k]+D[k][j])
 
        for i in range(self.n):
            for j in range(self.n):
                if D[i][j]==99999:
                    D[i][j]=-1
        
        return D
 
if __name__ == "__main__":
    a = AllRoutes(5)
    a.add_road(4,5,8)
    a.add_road(3,4,10)
    a.add_road(4,5,8)
    a.add_road(1,3,9)
    a.add_road(4,5,4)
    a.add_road(4,5,10)
    a.add_road(4,5,7)
    a.add_road(4,5,3)
    a.add_road(1,4,6)
    print(a.get_table())