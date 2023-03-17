"""
How many ways can an integer n be represented as a sum of positive integers? 

Two representations are considered different if they still differ when the terms of the sum are ordered. 

The sum may also consist of a single number.

For example the number 5 has the following seven representations: 5, 1+4, 2+3, 1+1+3, 1+2+2, 1+1+1+2 and 1+1+1+1+1.

You may assume that n is in the range 1...50. 

Your code must compute the answer on its own (for example, it should not use an array that contains all the answers).
"""

def count(n):
    listing=[]
    for i in range(n+1):
        if i==0:
            listing.append(1)
        else:
            listing.append(0)
 
    for x in range(n-1):
        for y in range(x+1,n+1):
            listing[y]+=listing[y-x-1]
    
    return listing[-1]+1
 
if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174