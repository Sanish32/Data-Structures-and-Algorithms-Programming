#Your task is to count the number of substrings in a string where all the characters are the same. 
#
#For example, the string abbbcaa has 11 such substrings:
#a (three times)
#aa
#b (three times)
#bb (twice)
#bbb
#c
#
#You may assume that the string consists of the characters a–z and contains at most 105 characters. 
#The goal is an algorithm with time complexity 𝑂(n).
#

def count(s):
    left=s[0]
    right=s[0]
    i=0
    j=0
    sum=0
    length=0
    comb=0
    t=True
    while t:
        try:
            if left==right:
                length+=1
                j+=1
                if j<len(s):
                    right=s[j]
                else:
                    t=False
            else:
                left=s[j]
                right=s[j]
                comb=((length)*(length+1))/2
                sum+=comb
                length=0
        except IndexError:
            return sum
    comb=((length)*(length+1))/2
    sum+=comb
    return int(sum)
 
if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5