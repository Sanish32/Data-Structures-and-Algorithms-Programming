"""
You are given numbers one at a time. 

After each number, your task is to report the mode (the most frequent number) among the numbers seen so far. 
If there are multiple modes, report the smallest of them.

You may assume that each number is an integer in the range 1...109 and that there are at most 105 numbers in total.
"""

class Mode:
    def __init__(self):
        self.dictionary={}
        self.freq=0
        self.number=0
 
    def add(self, x):
        if len(self.dictionary)==0:
            self.number=x
            self.freq=1
 
        if x in self.dictionary:
            self.dictionary[x]+=1
    
        else:
            self.dictionary[x]=1
 
        if self.dictionary[x]>=self.freq:
            if self.dictionary[x]>self.freq:
                self.freq=self.dictionary[x]
                self.number=x
            else:
                if x<self.number:
                    self.number=x
 
        return self.number
 
if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3