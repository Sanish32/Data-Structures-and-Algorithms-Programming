#You are given a list of numbers where each number occurs twice except one number occurs only once. 
#
#Your task is to find this odd number.
#
#Each element of the list is an integer in the range 1...109 and the list has at most 105 elements. 
#
#The goal is an algorithm with time complexity 𝑂(𝑛) or 𝑂(𝑛log𝑛).

def find(t):
    dict={}
    for i in range(len(t)):
        if t[i] not in dict:
            dict[t[i]]=1
        else:
            dict[t[i]]+=1
    for item in dict:
        if dict[item]!=2:
            return item 
 
if __name__ == "__main__":
    print(find([2,2,4,3,4])) # 3
    print(find([1,2,3,4,1,2,3])) # 4
    print(find([1])) # 1
    print(find([1,4,2,3,2,3,4])) # 1
    print(find([4,1,3,2,3,2,1])) # 4