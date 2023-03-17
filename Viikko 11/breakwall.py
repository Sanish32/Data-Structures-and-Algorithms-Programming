"""
You are given an 𝑛×𝑚 labyrinth and your task is to go from square A to square B.

Here the labyrinth has two kinds of walls: 
a wall at the border of the labyrinth is marked with # as before but internal walls are marked with *. 

You can break an internal wall to open new routes through the labyrinth.

What is the smallest number walls that you need to break in order to reach your goal? You may assume that 1≤n,m≤20.
"""

from heapq import heappop,heappush
 
 
def bfs(r,distance,u,v):
 
    Q=[]
    heappush(Q,(0,(u,v)))
 
    while len(Q)!=0:
        a=heappop(Q)
        d=a[0]
        x=a[1]
 
        if r[x[0]][x[1]]=="B":
            return d
 
        if x[1]+1<len(r[0])-1:
            if r[x[0]][x[1]+1]=="*":
                if distance[x[0]][x[1]+1]>d+1:
                    heappush(Q,(d+1,(x[0],x[1]+1)))
                    distance[x[0]][x[1]+1]=d+1
            else:
                if distance[x[0]][x[1]+1]>d:
                    distance[x[0]][x[1]+1]=d
                    heappush(Q,(d,(x[0],x[1]+1)))
                
        if x[0]+1<len(r)-1:
            if r[x[0]+1][x[1]]=="*":
                if distance[x[0]+1][x[1]]>d+1:
                    heappush(Q,(d+1,(x[0]+1,x[1])))
                    distance[x[0]+1][x[1]]=d+1
            else:
                if distance[x[0]+1][x[1]]>d:
                    distance[x[0]+1][x[1]]=d
                    heappush(Q,(d,(x[0]+1,x[1]))) 
 
        if x[1]-1>0:
            if r[x[0]][x[1]-1]=="*":
                if distance[x[0]][x[1]-1]>d+1:
                    heappush(Q,(d+1,(x[0],x[1]-1)))
                    distance[x[0]][x[1]-1]=d+1
            else:
                if distance[x[0]][x[1]-1]>d:
                    distance[x[0]][x[1]-1]=d
                    heappush(Q,(d,(x[0],x[1]-1)))
 
        if x[0]-1>0:
            if r[x[0]-1][x[1]]=="*":
                if distance[x[0]-1][x[1]]>d+1:
                    heappush(Q,(d+1,(x[0]-1,x[1])))
                    distance[x[0]-1][x[1]]=d+1
            else:
                if distance[x[0]-1][x[1]]>d:
                    distance[x[0]-1][x[1]]=d
                    heappush(Q,(d,(x[0]-1,x[1])))
 
def count(r):
    # TODO    
    x=0
    distance=[[99999]*len(r[0]) for _ in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j]=="A":
                distance[i][j]=0
                x=bfs(r,distance,i,j)
    
    return x
 
if __name__ == "__main__":
    r = ["##########",
         "#.*.**.**#",
         "#*.B*.*.*#",
         "#******..#",
         "#.****.**#",
         "#****A***#",
         "#********#",
         "#********#",
         "#**.****.#",
         "##########"]
    print(count(r)) # 2