#You are given a list of integers and your task is to count how many ways you can split the list into two parts so that every element in the left part is smaller than every element in the right part.
#
#For example the list [2,1,2,5,7,6,9] has 3 ways:
#[2,1,2] and [5,7,6,9]
#[2,1,2,5] and [7,6,9]
#[2,1,2,5,7,6] and [9]
#
#You may assume that each number in the list is in the range 1…109 and contains at most 105 elements. 
#The goal is an algorithm with time complexity 𝑂(n).
#

def count(t):
    maximums=[]
    c1=t[0]
    sum=0
    c2=t[0]
    minimus=[]
 
    for item in t:
        if item>c1:
            maximums.append(item)
            c1=item
        else:
            maximums.append(c1)
            
    t.reverse()
    c2=t[0]
    minimus=[]
    
    for item in t:
        if item<c2:
            minimus.append(item)
            c2=item
        else:
            minimus.append(c2)
    minimus.reverse()
    maximums.pop(-1)
    minimus.pop(0)
    
    for i in range(len(maximums)):
        if maximums[i]<minimus[i]:
            sum+=1
    return sum
if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3
    print(count([1,2,3,1])) # 0