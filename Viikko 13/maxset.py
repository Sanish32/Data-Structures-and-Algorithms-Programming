"""
Initially each of the numbers 1,2,…,𝑛 is in its own set. 

Your task is to implement a class that supports merging two sets and finding the largest set.

You may assume that n is at most 105 and that the methods of the class are called at most 105 times.
"""

class MaxSet:
    def __init__(self,n):
        # TODO
        self.n=n
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
        self.max=1
 
    def find(self, x):
        a=x
        while self.parent[x]!=x:
            x=self.parent[x]
        self.parent[a] = x
        return x
 
    def union(self, x, y):
        if self.size[x]>=self.size[y]:
            self.parent[y]=x
            self.size[x]=self.size[x]+self.size[y]
            if self.size[x]>self.max:
                self.max=self.size[x]
        else:
            self.parent[x]=y
            self.size[y]=self.size[x]+self.size[y]
            if self.size[y]>self.max:
                self.max=self.size[y]
 
    def merge(self,a,b):
        # TODO
        x=self.find(a)
        y=self.find(b)
        if x!=y:
            self.union(x,y)
 
    def get_max(self):
        # TODO
        return self.max
 
if __name__ == "__main__":
    #m = MaxSet(5)
    #print(m.get_max()) # 1
    #m.merge(1,2)
    #m.merge(3,4)
    #m.merge(3,5)
    #print(m.get_max()) # 3
    #m.merge(1,5)
    #print(m.get_max()) # 5
    m = MaxSet(100000)
    m.merge(73846,95230)
    m.merge(65689,91281)
    print(m.get_max())
    m.merge(56793,63652)
    m.merge(54686,67495)
    m.merge(46393,62264)
    m.merge(80760,96970)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(91852,98254)
    m.merge(69907,74715)
    m.merge(91092,91882)
    print(m.get_max())
    m.merge(41193,70278)
    print(m.get_max())
    m.merge(4474,49377)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(58372,93525)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(15274,92644)
    m.merge(1733,22362)
    m.merge(40269,70325)
    m.merge(88469,91735)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(13142,84949)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(80264,88691)
    m.merge(45648,55883)
    m.merge(52198,90801)
    print(m.get_max())
    m.merge(38246,91212)
    m.merge(98587,99083)
    m.merge(82946,92201)
    m.merge(26088,51679)
    print(m.get_max())
    print(m.get_max())
    m.merge(23272,25808)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(74161,97911)
    print(m.get_max())
    m.merge(874,49821)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(49359,69736)
    m.merge(2262,82351)
    print(m.get_max())
    m.merge(14065,38027)
    print(m.get_max())
    print(m.get_max())
    m.merge(99253,99731)
    print(m.get_max())
    m.merge(73053,76582)
    print(m.get_max())
    m.merge(53476,71491)
    m.merge(53513,60286)
    m.merge(20962,48423)
    print(m.get_max())
    print(m.get_max())
    m.merge(67072,75995)
    m.merge(4328,80126)
    m.merge(77744,78417)
    print(m.get_max())
    m.merge(76121,93753)
    print(m.get_max())
    m.merge(77708,95007)
    m.merge(97693,98661)
    m.merge(67975,95602)
    print(m.get_max())
    print(m.get_max())
    m.merge(45715,45987)
    print(m.get_max())
    m.merge(59374,62955)
    print(m.get_max())
    m.merge(25763,55654)
    m.merge(43317,75375)
    m.merge(69730,87799)