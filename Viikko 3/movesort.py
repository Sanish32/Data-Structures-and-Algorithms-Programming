#The list is a permutation of the numbers 1,2,…,𝑛, where 𝑛 is even. 
#
#Your task is to find out if the list can be sorted using operations of the following kind: 
#
#Choose an integer in the range 1…𝑛/2 and swap the first 𝑖 elements of the list with the last 𝑖 elements maintaining the order.
#
#For example when 𝑛=4, the list [3,1,4,2] can be sorted as follows:
#[3,1,4,2]⟶[4,2,3,1]⟶[1,2,3,4]
#
#Here 𝑖=2 in the first operation and 𝑖=1 in the second operation. 
#On the other hand, the list [3,1,2,4] cannot be sorted with any sequence of operations.
#
#You may assume that 𝑛 is in the range 2...105. 
#
#The goal is an algorithm with time complexity 𝑂(𝑛) or 𝑂(𝑛log𝑛)

def check(t):
    list1=[]
    list2=[]
    for i in range((len(t)//2)-1):
        list1.append(t[i]-t[i+1])
    
    for i in range(len(t)//2,len(t)-1):
        list2.append(t[i]-t[i+1])
    a=True
    list2.reverse()
    for i in range((len(t)//2)-1):
        if list1[i]!=list2[i]:
            a=False
    if a:
        return True
    return False
if __name__ == "__main__":
    print(check([3,1,4,2])) # True
    print(check([3,1,2,4])) # False
    print(check([1,2])) # True
    print(check([4,5,6,1,2,3])) # True
    print(check([4,5,6,3,2,1])) # False
    print(check([5, 8, 13, 1, 3, 6, 11, 4, 9, 12, 14, 2, 7, 10]))