class Student:
    def __init__(self,name,roll,branch):
        self.name=str(name)
        self.roll=roll
        self.branch=branch
        print('Name:',self.name,'\tRoll No :',self.roll,'\tBranch :',self.branch)
        str1=[]
        str1.append(self.name)
        
    def names(self):
        print(str1)
        
        

student1=Student('Sagar',18,'E&TC')


