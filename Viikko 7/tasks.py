#Your task is to implement an efficient data structure for keeping a task list. 
#
#You can add a new task with a name and a priority to the list, and you can extract the highest priority task from the list.
#
#You may assume that the name of a task consists of the characters a–z and 0–9 and that the priority is an integer in the range 0...109. 
#
#The highest numeric value has the highest priority.
#

import heapq
class Tasks : 
    def __init__(self):
        self.listing=[]
        
 
    def add ( self , name , priority ): 
        heapq.heappush(self.listing,(-priority,name))
        
    def next ( self ): 
        x=heapq.heappop(self.listing)
        return x[1]
 
        
        
 
if __name__ == "__main__" : 
    t = Tasks()
    t.add("task1",1)
    t.add("task2",1)
    t.add("task3",1)
    t.add("task4",1)
    print(t.next())
    print(t.next())
    print(t.next())
    print(t.next())