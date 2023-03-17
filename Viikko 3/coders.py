#Group A has 𝑛 coders and group B has 𝑛 coders too. 
#Your task is to form 𝑛 pairs that each contain one coder from group A and one from group B. 
#Each coder must be included in exactly one pair.
#
#Each coder has a skill level, and the skill levels within a pair should similar.
#
#If the skill levels of a pair are 𝑥 and 𝑦, this causes a penalty of |𝑥−𝑦|.
#
#Your goal is to find a solution that minimizes the total sum of the penalties.
#
#You may assume that 𝑛 is at most 105 and that each skill level is an integer in the range 1...109. 
#
#The goal is an algorithm with time complexity 𝑂(𝑛) or 𝑂(𝑛log𝑛).
#

def find(a,b):
    a.sort()
    b.sort()
    sum=0
    for i in range(len(a)):
        sum+=abs(a[i]-b[i])
    return sum
 
if __name__ == "__main__":
    print(find([1,2,3],[2,5,2])) # 3
    print(find([2],[7])) # 5
    print(find([1,1,1,1],[3,4,3,4])) # 10
    print(find([5,2,9,1,2,4],[8,8,2,3,9,4])) # 11