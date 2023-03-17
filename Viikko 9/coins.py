"""
You have n coins and each coin has an integral value. 

Your task is to count how many sums you can form using the coins.

For example, if the coins are [3,4,5], there are 7 possible sums: 
3, 4, 5, 7, 8, 9 and 12. 

Notice that a sum must have at least one coin, i.e., an empty set is not counted.

You may assume that 1≤n≤100 and that each coin has a value in the range 1..100.
"""

def count(t):
    counting=0
    arr=[]
    
    if len(t)==1:
        return 1
    for i in range(len(t)):
        arr.append([False]*(sum(t)+1))
 
    for i in range(len(t)):
        arr[i][t[i]]=True
        for j in range(sum(t)+1):
            if arr[i-1][j]==True:
                arr[i][j+t[i]]=True
                arr[i][j]=True
 
    for i in range(sum(t)+1):
        if arr[-1][i]==True:
            counting+=1
 
    return counting
 
if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91