"""
You are given an nxm grid that represents a labyrinth. 

Your task is to determine the length of the shortest route from the square A to the square B. 

Each square is either floor (.) or wall (#), and all squares at the edges of the grid are walls.

You may assume that 1≤n,m≤20. 

If there is no path, return -1.
"""

from collections import deque

def bfs(r,graph,distance,u,v):
    counting=[]
    for i in range(len(r)):
        for j in range(len(r[0])):
            graph[i][j]=False
            distance[i][j]=0
    graph[u][v]=True
    distance[u][v]=0
 
    Q=deque()
    Q.append((u,v,distance[u][v]))
 
    while len(Q)!=0:
        x=Q.popleft()
        if x[1]+1<len(r[0]) and graph[x[0]][x[1]+1]==False:
            if r[x[0]][x[1]+1]==".":
                graph[x[0]][x[1]+1]=True
                distance[x[0]][x[1]+1]=distance[x[0]][x[1]]+1
                Q.append((x[0],x[1]+1,distance[x[0]][x[1]+1]))
                
        if x[0]+1<len(r) and graph[x[0]+1][x[1]]==False:
            if r[x[0]+1][x[1]]==".":
                graph[x[0]+1][x[1]]=True
                distance[x[0]+1][x[1]]=distance[x[0]][x[1]]+1
                Q.append((x[0]+1,x[1],distance[x[0]+1][x[1]]))
 
        if x[1]-1>=0 and not graph[x[0]][x[1]-1]:
            if  r[x[0]][x[1]-1]==".":
                graph[x[0]][x[1]-1]=True
                distance[x[0]][x[1]-1]=distance[x[0]][x[1]]+1
                Q.append((x[0],x[1]-1,distance[x[0]][x[1]-1]))
 
        if x[0]-1>=0 and not graph[x[0]-1][x[1]]:
            if r[x[0]-1][x[1]]==".":
                graph[x[0]-1][x[1]]=True
                distance[x[0]-1][x[1]]=distance[x[0]][x[1]]+1
                Q.append((x[0]-1,x[1],distance[x[0]-1][x[1]])) 
 
 
        if x[1]+1<len(r[0]) and graph[x[0]][x[1]+1]==False:
            if r[x[0]][x[1]+1]=="B":
                distance[x[0]][x[1]+1]=distance[x[0]][x[1]]+1
                counting.append(distance[x[0]][x[1]+1])       
    
        if x[0]+1<len(r) and graph[x[0]+1][x[1]]==False:
            if r[x[0]+1][x[1]]=="B":
                distance[x[0]+1][x[1]]=distance[x[0]][x[1]]+1
                counting.append(distance[x[0]+1][x[1]])       
 
 
        if x[1]-1>=0 and not graph[x[0]][x[1]-1]:
            if  r[x[0]][x[1]-1]=="B":
                distance[x[0]][x[1]-1]=distance[x[0]][x[1]]+1
                counting.append(distance[x[0]][x[1]-1])       
 
        if x[0]-1>=0 and not graph[x[0]-1][x[1]]:
            if r[x[0]-1][x[1]]=="B":
                distance[x[0]-1][x[1]]=distance[x[0]][x[1]]+1
                counting.append(distance[x[0]-1][x[1]])       
    if len(counting)==0:
        return -1
    return min(counting)
 
def count(r):
    # TODO
    distance=[[0]*len(r[0]) for _ in range(len(r))]
    graph=[[False]*len(r[0]) for _ in range(len(r))]
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j]=="A":
                x=bfs(r,graph,distance,i,j)
                break
    return x
 
if __name__ == "__main__":
    r = ["##########",
         "#...#....#",
         "#..##...##",
         "#..#.....#",
         "##..#.#..#",
         "#.#.....##",
         "#..A#..B.#",
         "###....#.#",
         "#....#.#.#",
         "##########"]
    print(count(r)) # 7