#You are given a list of 𝑛 numbers, and an additional number 𝑥. 
#
#How many ways can you form a pair of numbers with the numbers taken from two different positions on the list and summing up to at most 𝑥?
#
#You may assume that 𝑛 is at most 105 and that each number on the list as well as 𝑥 is an integer in the range 1...109. 
#
#The goal is an algorithm with time complexity 𝑂(𝑛) or 𝑂(𝑛log𝑛).
#

def find(t,x):
    t.sort()
    check=len(t)
    sum=0
    a=check
    start=t[0]
    j=0
    while j < check-1:
        if start+t[check-1]<=x:
            sum+=check-1-j
            j+=1
            start=t[j]
        else:
            check-=1
 
    return sum
if __name__ == "__main__":
    print(find([2],1))
    print(find([1,2,3],4)) # 2
    print(find([5,2,4,7],10)) # 4
    print(find([1,1,1,1],2)) # 6
    print(find([1,1,1,1],1)) # 0
    print(find([8,8,1,2,5,1,9,3],9)) # 14