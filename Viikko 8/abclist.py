"""
Your task is to construct a list that contains all strings of length n consisting of the characters A, B and C. 

The list must be in alphabetical order.

You may assume that n is in the range 1...10.
"""

def go(listing,n,adding):
    i=0
    for i in range(3**n):
        listing[i]+=adding[i%3]
 
def create(n):
    listing=[]
    adding=["A","B","C"]
    i=0
    j=0
    for i in range(3**n):
        listing.append(adding[i%3])
        
    while len(listing[0])!=n:
        listing.sort()
        go(listing,n,adding)
    return listing
 
if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243