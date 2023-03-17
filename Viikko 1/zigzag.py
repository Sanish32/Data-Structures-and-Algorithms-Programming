#Insert the numbers 1,2,…,n into a list starting with 1 and then inserting the following numbers 
# alternatingly to the right end and to the left end. 
#
#For example when n =5the result is [5,3,1,2,4].
#
#What does the list look like for a given n? You may assume that 1≤n≤1000
#

def create(n):
    new=[]
    for i in range(1,n+1):
        if i%2==1:
            new.insert(0,i)
        else:
            new.append(i)
 
    return new
 
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]