#This is an English translation of the CSES problem Onnenluvut.
#
#A positive integer is a lucky number (onnenluku in Finnish) if the sum of its digits is divisible by 7. 
#
#For example, 25743 is a lucky number because 2+5+7+4+3=21 which is divisible by 7.
#
#Your task is to check whether a given number n is a lucky number. You may assume that n is an integer in the range 1...109.
#

def check (n):
    words=str(n)
    sum=0
    for i in range(len(words)):
        sum+=int(words[i])
 
    if sum%7==0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print (check (14)) # Falseprint ( check ( 14 )) # False 
    print (check (16)) # Trueprint ( check ( 16 )) # True 
    print (check (123)) # Falseprint ( check ( 123 )) # False 
    print (check (777)) # Trueprint ( check ( 777 )) # True 
    print (check (9999999)) # Trueprint ( check ( 9999999 )) # True 