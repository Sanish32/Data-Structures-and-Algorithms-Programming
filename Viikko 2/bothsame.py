#Your task is to count the number of substrings in a string where the first and the last character are the same. 
#
#For example, the string ababca has 10 such substrings:
#a (three times)
#aba
#ababca
#abca
#b (twice)
#bab
#c
#
#You may assume that the string consists of the characters a–z and contains at most 105 characters. 
#The goal is an algorithm with time complexity 𝑂(n).
#

def count(s):
    j=0
    sum=0
    length=0
    comb=0
    new=[item for item in s]
    new.sort()
    word="".join(new)
    left=word[0]
    right=word[0]
    t=True
    while t:
        try:
            if left==right:
                length+=1
                j+=1
                if j<len(word):
                    right=word[j]
                else:
                    t=False
            else:
                left=word[j]
                right=word[j]
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
    print(count("abcd")) # 4
    print(count("ababca")) # 10
    print(count("babbbabbba"))