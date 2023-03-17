"""
Your task is to design a class that supports adding courses and their prerequisite relations, 
and finding a way to take the courses in an order that satisfies the requisites.

If there are multiple orders, any of them is acceptable.

You may assume that the number of courses is at most 50 and that the methods of the class are called at most 100 times. 

The name of each course is a string of at most 10 characters.
"""

class CoursePlan:
    def __init__(self):
        # TODO
        self.courses=[]
        self.n=0
        self.courseplan=[]
        self.checker=False
 
    def add_course(self,course):
        # TODO
        self.courses.append(course)
        self.courseplan.append([])
        self.n+=1
 
    def add_requisite(self,course1,course2):
        # TODO
        if course1==course2:
            self.checker=True
        
        for i in range(len(self.courses)):
            if self.courses[i]==course1:
                self.courseplan[i].append(course2)
                break
 
    def DFS(self,i,u):
        self.color[i]="gray"
 
        for v in self.courseplan[i]:
            for j in range(len(self.courses)):
                if self.courses[j]==v:
                    if self.color[j]=="gray":
                        self.checker=True
                        return
                    elif self.color[j]=="white":
                        self.DFS(j,v)
                        if self.checker==True:
                            return 
                    break   
                
        self.color[i]="black"
        if u not in self.ordering:
            self.ordering.insert(0,u)
 
    def find(self):
        # TODO
        self.ordering=[]
        if self.checker==True:
            return None
 
        self.checker=False
        self.color=["white"]*(self.n)
 
        for v in range(self.n):
            if self.color[v]=="white":
                self.DFS(v,self.courses[v])
                if self.checker==True:
                    return None
 
        return self.ordering
 
if __name__ == "__main__":
    c = CoursePlan()
    c.add_course('course3')
    c.add_course('course1')
    c.add_requisite('course3','course1')
    print(c.find())
    print(c.find())
    c.add_course('course5')
    c.add_requisite('course5','course3')
    print(c.find())