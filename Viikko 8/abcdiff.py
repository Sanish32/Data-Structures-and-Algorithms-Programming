"""
Your task is to construct a list that contains all strings of length n consisting of the characters A, B and C so that two adjacent characters are never the same. 

The list must be in alphabetical order.

You may assume that n is in the range 1...10.
"""

def add(word, length, listing):
    if len(word) == length:
        listing.append(word)
    else:
        if len(word)==0 or word[-1]!="A":
            add(word+"A", length, listing)
        if len(word)==0 or word[-1]!="B":
            add(word+"B", length, listing)
        if len(word)==0 or word[-1]!="C":
            add(word+"C", length, listing)
 
def create(n):
    listing = []
    add("", n, listing)
 
    return listing
 
if __name__ == "__main__":
    #print(create(1)) # [A,B,C]
    #print(create(2)) # [AB,AC,BA,BC,CA,CB]
    #print(create(3))
    print(len(create(5))) # 48
    print(len(create(10)))