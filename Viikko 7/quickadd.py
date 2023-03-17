#Your task is to implement a data structure that maintains a collection of numbers. 
#
#The data structure supports efficiently adding 𝑘 copies of a number 𝑥, as well as removing the k smallest numbers and returning their sum.
#
#You may assume that 𝑘 and 𝑥 are in the range 0...109 in each operation.
#

from heapq import heappush,heappop
 
class QuickAdd : 
    def __init__(self):
        self.tasks=[]
 
    
    def add ( self , k , x ): # TODO 
        heappush(self.tasks,(x,k))
        
 
    def remove ( self , k ): # TODO
        x,y=heappop(self.tasks)
        sum=0
        if k<=y:
            sum=x*k
            y-=k
            if y!=0:
                heappush(self.tasks,(x,y))
        elif k>y:
            k-=y
            sum+=self.remove(k)
            sum+=x*y
        
        return sum
        
 
if __name__ == "__main__" : 
    q=QuickAdd() 
    q.add(5,3) 
    print(q.remove(2)) # 6 
    q.add(8,1) 
    print(q.remove(4)) # 4 
    print(q.remove(7)) # 13 
    q.add(10**9,123) 
    print(q.remove(10**9)) # 123 billion