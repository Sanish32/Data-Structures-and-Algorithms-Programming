"""
You are given an 𝑛×𝑚 grid that represents a map of a house. 

Each square is either floor (.) or wall (#), and all squares at the edges of the grid are walls.

Two floor squares belong to the same chamber if they are adjacent on the same row or column. 
How many chambers are there?

You may assume that 1≤n,m≤20.
"""

def dfs(r,graph,u,v):
    graph[u][v]=True
    if v+1<len(r[0]) and graph[u][v+1]==False:
        if r[u][v+1]==".":
            dfs(r,graph,u,v+1)
    if u+1<len(r) and graph[u+1][v]==False:
        if r[u+1][v]==".":
            dfs(r,graph,u+1,v)
    if v-1>=0 and not graph[u][v-1]:
        if  r[u][v-1]==".":
            dfs(r,graph,u,v-1)
    if u-1>=0 and not graph[u-1][v]:
        if r[u-1][v]==".":
            dfs(r,graph,u-1,v)
 
def count(r):
    # TODO
    graph=[[False]*len(r[0]) for _ in range(len(r))]
    counting=0
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j]=="." and graph[i][j]==False:
                dfs(r,graph,i,j)
                counting+=1
    
    return counting 
 
if __name__ == "__main__":
    r = ["##########",
         "#.#...#.##",
         "#..#...#.#",
         "###...#..#",
         "#.##...#.#",
         "##.......#",
         "#.##.....#",
         "#..#.#.#.#",
         "#..##.#.##",
         "##########"]
    print(count(r)) # 7