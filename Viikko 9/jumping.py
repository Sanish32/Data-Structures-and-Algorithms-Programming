""" 
You are playing a game with n levels. 

Initially you are at level 0 and your goal is to reach level n. In each step, you can jump a or b levels up. How many ways are there to reach the level n?

For example, when n=4, a=1 and b=2, there are 5 ways:
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4
0 → 1 → 3 → 4
0 → 2 → 3 → 4
0 → 2 → 4

You may assume that 3≤n≤50 and 1≤a<b≤n.
"""

def count(n,a,b):
    arr=[0]*(n+1)
    arr[a]=1
    arr[b]=1
    for i in range(len(arr)):
        if i-a>0:
            arr[i]+=arr[i-a]
        if i-b>0:
            arr[i]+=arr[i-b]
    return arr[-1]
 
if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456
 