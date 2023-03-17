#Your task is to find out how long is the shortest string that forms the given string when repeated. 
#
#For example, when the input string is abcabcabcabc, the shortest repeated string is abc.
#
#The string consists of the characters a–z and contains at most 100 characters.
#

def find(s):
    length=0
    given=s[:]
    for i in range(0,len(s)):
        length+=1
    for i in range(0, length):
        if length%(i+1)==0 and (given[:i+1]*(length//(i+1)))==given:
            return i+1
 
if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7