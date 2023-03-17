"""
You are given water containers with the capacities of a and b liters, and your task is to measure x liters using the containers.

Initially the containers are empty and they have no measuring scale. 

In each step, you can fill or empty one of the containers or pour water from one container to the other, 
but only so that one of the containers becomes full or empty, because otherwise the measurement would not be exact.

What is the smallest amount of water to move to measure exactly x liters into the first container? 

For example when a=5, b=4 and x=2, the smallest amount is 22 liters. 

Here is one optimal solution:
Fill the first container (5 liters of water moved)
Pour from the first container to the second one (4 liters of water moved)
Empty the second container (4 liters of water moved)
Pour the contents of the first container into the second one (1 liter of water moved)
Fill the first container (5 liters of water moved)
Pour from the first container to the second one (3 liters of water moved)
"""

def checker(a,b,x, marker):
    check=False
 
    d=a
    e=0
    needed=a
 
    if d==marker:
        check=True
 
    while (e!=x) and (d!=x):
 
        temp = min(d,b-e)
        e+=temp
        d-=temp
 
        needed+=temp
        
        if (e==x) or (d==x):
            if check:
                if d==x:
                    break
 
                elif d==0:
                    needed+=e
                    break
 
                else:
                    needed+=d
                    needed+=e
                    break
            else:
                if e==x:
                    break
 
                elif e==0:
                    needed+=d
                    break
 
                else:
                    needed+=e
                    needed+=d
                    break
 
        if d==0:
            d=a
            needed+=d
 
        if e==b:
            needed+=b 
            e=0
 
    return needed
 
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)
 
def count(a,b,x): 
    if a<x:
        return -1
 
    if a==x:
        return x
        
    if b==x:
        return 2*x
 
    if x%(gcd(a,b))!=0:
        return -1
 
    marker=a
    return (min(checker(a,b,x, marker), checker(b,a,x, marker)))
 
if __name__ == "__main__":
    print(count(5,4,2)) # 22
    print(count(4,3,2)) # 16
    print(count(3,3,1)) # -1
    print(count(10,9,8)) # 46
    print(count(123,456,42)) # 10530