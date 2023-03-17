"""
You are given a list containing n distinct integers. 

Your task is find out the kth smallest distance between two of the numbers, where all possible pairs of numbers are considered.

For example when the list is [4,1,5,2], the distances from the smallest to the largest are:
numbers 1 and 2 have a distance 1
numbers 4 and 5 have a distance 1
numbers 2 and 4 have a distance 2
numbers 1 and 4 have a distance 3
numbers 2 and 5 have a distance 3
numbers 1 and 5 have a distance 4

You may assume that n is at most 105, that each number is in the range 1...109, and that k is at most 105.
"""

import heapq 
def find(t, k):
    listing=[]
    t.sort()
    for i in range(1,len(t)):
        diff=abs(t[i]-t[i-1])
        heapq.heappush(listing,(diff,i-1,i))
 
    for i in range(k):
        x=heapq.heappop(listing)
        if (x[2]+1)<len(t):
            y=abs(t[x[2]+1]-t[x[1]])
            heapq.heappush(listing,(y,x[1],x[2]+1))
    return x[0]
 
if __name__ == "__main__":
    t = [4,1,5,2]
    print(find(t,1)) # 1
    print(find(t,2)) # 1
    print(find(t,3)) # 2
    print(find(t,4)) # 3
    print(find(t,5)) # 3
    print(find(t,6)) # 4
    