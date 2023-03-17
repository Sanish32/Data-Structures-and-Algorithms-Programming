"""
Your task is to construct a list that contains all the anagrams of a given string, i.e. all the strings consisting of the same letters as the original. 

The list must be in alphabetical order.

You may assume that the string consists of the letters a-z and has at most 8 characters.
"""

from itertools import permutations
 
def create(s):
    needed=[]
    word=""
    for item in permutations(s):
        if item not in needed:
            word="".join(item)
        if word not in needed:
            needed.append(word)
    needed.sort()
    return needed
if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260