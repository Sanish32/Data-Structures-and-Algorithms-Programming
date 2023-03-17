#The numbers 1,2,...,n are add to a max heap in increasing order. 
#
#How many swaps of two elements are performed during the whole process? 
#
#You may assume that n is at most 109. (Note: Assume the version of heap insertion that uses swaps of elements.)
#
#For example when n=4, the swaps are 1↔2, 2↔3, 1↔4 and 3↔4, and so the answer is 4.
#

from math import floor, log2
def count ( n ): # TODO
    if n==0 or n==1:
       return 0
 
    count=0
    l=log2(n+1)
    l=floor(l)
    
    if (2**l)-1<n:
        count=l*(n+1-(2**l))
 
    for i in range(1,l+1):
        count+=(i-1)*(((2**i)-1)-((2**(i-1))-1))
 
    return count
 
if __name__ == "__main__":
    print(count(4)) # 4
    print(count(7)) # 10
    print(count(123)) # 618
    print(count(999999999)) # 27926258178