#Initially the list content is [1,2,3,...,n]. In each step, you extract the first two elements of the list and insert them at the end of the list in reverse order. 
#
#What is the first element of the list after k steps?
#
#For example when n=4 and k=3, the list changes as follows:
#[1,2,3,4] → [3,4,2,1] → [2,1,4,3] → [4,3,1,2]
#
#Thus, in this case, the first element is 4.
#
#You may assume that n is in the range 2...105 and that k is at most 105. 
#The goal is an algorithm with time complexity 𝑂(𝑛+𝑘).
#

from collections import deque
def solve(n,k):
    q=deque()
    for i in range(n):
        q.append(i+1)
 
    for i in range(k):
        a=q.popleft()
        b=q.popleft()
        q.append(b)
        q.append(a)
    return q[0]
 
if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875