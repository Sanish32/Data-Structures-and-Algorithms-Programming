#The pseudocode given at the CSES assignment represents a function count that computes the number of primes in the range 2..n.
#

def count(n):
    # TODO
    prime=[]
    for i in range(2,n+1):
        logic=True
        for j in range(len(prime)):
            if i%prime[j]==0:
                logic=False
                break
        if logic:
            prime.append(i)
    return len(prime)
 
if __name__ == "__main__":
    print(count(2)) # 1
    print(count(10)) # 4
    print(count(11)) # 5
    print(count(100)) # 25
    print(count(1000)) # 168