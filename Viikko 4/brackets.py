#Each character in a string is either ( or ). 
#
#In each step, you remove the left-most occurrence of the substring (). 
#Continue until you can no more remove anything. How many characters are left in the string?
#
#For example, when the string is ((())(, it first changes into (()( and then into ((. 
#In this case, the final string has 2 characters.
#
#You may assume that the string has at most 105 characters. 
#
#The goal is an algorithm with time complexity 𝑂(𝑛).
#

from collections import deque
def count(s):
    stack=deque()
    length=len(s)
    sum=0
    i=0
    for item in s:
        i+=1
        if item=="(":
            stack.append(item)
        else:
            if len(stack)==0 and i==len(s):
                return length
            if item==")" and len(stack)==0:
                stack.append(item)
            else:
                check=stack.pop()
                if check=="(" and item!=")":
                    pass
                elif check=="(" and item==")":
                    length-=2
    return length
            
    
if __name__ == "__main__":
    print(count("(()())")) # 0
    print(count(")))))")) # 5
    print(count("((())(")) # 2
    print(count("(()()())()()")) # 0
    print(count("))))))((((((")) # 12 
    print(count(")()))))()("))