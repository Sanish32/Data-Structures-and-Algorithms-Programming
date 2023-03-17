#Your task is to implement your own efficient data structure flip list that supports the following operations:
#Insert an element at the end of the list
#Return and delete the last element
#Insert an element to the beginning of the list
#Return and delete the first element
#Invert the order of the list
#
#Each operation should have a time complexity O(1). 
#
#You may assume that each element is an integer in the range 1...109.
#

from collections import deque
from re import T
import re
class FlipList:
    def __init__(self):
        self.listing=deque()
        self.T_F=True
 
    def push_last(self,x):
        if self.T_F:
            self.listing.append(x)
        else:
            self.listing.appendleft(x)
 
    def push_first(self,x):
        if self.T_F:
            self.listing.appendleft(x)
        else:
            self.listing.append(x)
 
    def pop_last(self):
        if self.T_F:
            return self.listing.pop()
        return self.listing.popleft()
 
    def pop_first(self):
        if self.T_F:
            return self.listing.popleft()
        return self.listing.pop()
 
    def flip(self):
        if self.T_F:
            self.T_F=False
        else:
            self.T_F=True
       
 
if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(5)
    f.push_last(3)
    f.flip()
    print(f.pop_last())
    print(f.pop_last())
    print(f.pop_last())