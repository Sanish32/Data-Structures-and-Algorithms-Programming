"""
You are given a list of n numbers. 

Your task is to count from left to right for each sublist of length k, how many distinct numbers it contains.

For example, when the list is [1,2,3,2,2,2] and k=3, the windows are [1,2,3], [2,3,2], [3,2,2] and [2,2,2]. 
These windows have 3, 2, 2 and 1 distinct numbers.

You may assume that n is at most 105, that each number is in the range 1...109, and that 1≤k≤n.
"""

def count(t,k):
    dict={}
    length=len(t)
    listing=[]
    for i in range(k):
        if t[i] not in dict:
            dict[t[i]]=1
        elif t[i] in dict:
            dict[t[i]]+=1
    listing.append(len(dict))
 
    for i in range(k,length):
        dict[t[i-k]]-=1
        if t[i] in dict:
            dict[t[i]]+=1
        else:
            dict[t[i]]=1
            
        
        if dict[t[i-k]]==0:
            dict.pop(t[i-k])
        listing.append(len(dict))
       
    return listing
if __name__ == "__main__":
    #print(count([1,1,2,2],2)) # [1,2,1]
    #print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]