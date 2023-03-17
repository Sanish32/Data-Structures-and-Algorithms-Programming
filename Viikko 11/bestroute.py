"""
Bitland has n cities that initially have no connecting roads. 

Your task is to design a class that supports adding a road between two cities and finding the shortest route between two cities.

All the roads go both directions and thus the order of the two cities makes no difference.

You may assume that the number of cities is at most 50 and that the methods of the class are called at most 100 times. 

The length of each road is an integer in the range 1...1000.
"""

from heapq import heappop, heappush

class BestRoute:
    def __init__(self,n):
        # TODO
        self.n=n
        self.adjacencylist=[[] for _ in range(self.n+1)]
        self.dict={}
 
    def add_road(self,a,b,x):
        # TODO
        word1=str(a)+str(b)
        word2=str(b)+str(a)
        if word1 not in self.dict:
            self.adjacencylist[a].append(b)
            self.adjacencylist[b].append(a)
            self.dict[word1]=x
            self.dict[word2]=x
        else:
            if self.dict[word1]>x:
                self.dict[word1]=x
                self.dict[word2]=x
 
    def find_route(self,a,b):
        # TODO
 
        if len(self.adjacencylist[a])==0 or len(self.adjacencylist[b])==0:
            return -1
 
        distance=[]
        processed=[]
        for i in range(1,self.n+2):
            distance.append(10000000000)
            processed.append(False)
            
        distance[a]=0
        heap=[]
        heappush(heap,(0,a))
        while len(heap)!=0:
            next=heappop((heap))
            u=next[1]
            if not processed[u]:
                processed[u]=True
                for edge in self.adjacencylist[u]:
                    v=edge
                    word=str(u)+str(v)
                    if distance[v]>distance[u]+self.dict[word]:
                        distance[v]=distance[u]+self.dict[word]
                        heappush(heap,(distance[v],v))
                      
        for i in range(len(distance)):
            if distance[i]==10000000000:
                distance[i]=-1
            
        return distance[b]
            
if __name__ == "__main__":
    b = BestRoute(50)
    b.add_road(22,26,51)
    b.add_road(30,45,482)
    b.add_road(37,38,202)
    b.add_road(40,46,737)
    b.add_road(16,23,738)
    b.add_road(31,34,891)
    b.add_road(15,47,635)
    b.add_road(26,50,286)
    b.add_road(43,50,507)
    b.add_road(20,22,709)
    b.add_road(17,40,760)
    b.add_road(34,36,840)
    b.add_road(39,42,631)
    b.add_road(31,45,221)
    b.add_road(10,43,903)
    b.add_road(41,48,842)
    b.add_road(17,38,88)
    b.add_road(36,46,54)
    b.add_road(25,27,879)
    b.add_road(41,49,293)
    b.add_road(3,5,477)
    b.add_road(44,48,405)
    b.add_road(40,50,692)
    b.add_road(20,38,110)
    b.add_road(15,46,579)
    b.add_road(38,46,31)
    b.add_road(12,49,423)
    b.add_road(21,23,76)
    b.add_road(26,35,54)
    b.add_road(34,40,284)
    b.add_road(27,42,58)
    b.add_road(17,18,476)
    b.add_road(45,49,728)
    b.add_road(41,43,514)
    b.add_road(5,39,10)
    b.add_road(29,33,838)
    b.add_road(21,26,582)
    print(b.find_route(45,48))