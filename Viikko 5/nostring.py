"""
You are given a string of n characters from the range a-z.

Your task is to find out how long is the shortest string that does not appear as a contiguous substring in the given string.

You may assume that n is at most 105.
"""


from string import ascii_lowercase
 
def find(s):
    for i in ascii_lowercase:
        if i not in s:
            return 1
 
    listing=[]
    for i in ascii_lowercase:
        for j in ascii_lowercase:
            listing.append(i+j)
    
    for item in listing:
        if item not in s:
            return 2
        
    listing.clear()
    for i in ascii_lowercase:
        for j in ascii_lowercase:
            for k in ascii_lowercase:
                listing.append(i+j+k)
    
    for item in listing:
        if item not in s:
            return 3
            
    return 4
if __name__ == "__main__":
    print(find("zzz")) # 1
    print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2