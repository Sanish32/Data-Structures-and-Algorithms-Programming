#Your task is to count how many different ways one can place a queen and a knight on a chess board of size nxn 
#so that neither piece threatens the other
#
#You may assume that n is at most 20.
#

def count(n):
    combination=0
    count=0
    queen=[]
    for i in range(n):
        queen.append([])
    for item in queen:
        for j in range(n):
            item.append(1)
 
 
    while count<n:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    queen[i][k]=0
                    queen[k][j]=0
 
                    if j+1<n and i+2<n:
                        queen[i+2][j+1]=0
                    if j+2<n and i+1<n:    
                        queen[i+1][j+2]=0
                    if j-2>=0 and i+1<n:
                        queen[i+1][j-2]=0 
                    if  j-1>=0 and i+2<n:
                        queen[i+2][j-1]=0
                    if  j-1>=0 and i-2>=0:
                        queen[i-2][j-1]=0 
                    if  j-2>=0 and i-1>=0:
                        queen[i-1][j-2]=0 
                    if j+2<n and i-1>=0:
                        queen[i-1][j+2]=0 
                    if j+1<n and i-2 >=0:
                        queen[i-2][j+1]=0 
                    
                        
                    if j-k>=0 and i-k>=0:
                        queen[i-k][j-k]=0
                    if j+k<n and i+k<n : 
                        queen[i+k][j+k] = 0
                    if j+k<n and i-k >=0:
                        queen[i-k][j+k]=0
                    if j-k>=0 and i+k<n:
                        queen[i+k][j-k]=0
 
                count+=1
 
                for a in queen:
                    for b in a:
                        combination+=b    
                    
                for a in queen:
                    a.clear()
 
                for item in queen:
                    for j in range(n):
                        item.append(1)
    return combination
 
if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184