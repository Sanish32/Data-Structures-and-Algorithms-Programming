#A robot is initially in the square (0,0).
# 
#The robot then moves step by step according to a given sequence of commands. 
#The sequence consists of the symbols U (up), D (down), L (left) and R (right). 
#
#How many distinct squares does the robot visit?
#
#You may assume that the sequence contains at most 105 commands.
#

def count ( s ): # TODO
    x=0
    y=0
    listing=[(0,0)]
    for item in s:
        if item=="U":
            y+=1
        elif item=="D":
            y-=1
        elif item=="L":
            x+=1
        elif item=="R":
            x-=1
        listing.append((x,y))    
    return len(set(listing))
if __name__=="__main__":
    print ( count ( "LL" )) # 3 
    print ( count ( "UUDLRR" )) # 5 
    print ( count ( "UUDUDUDU" )) # 3
 
 