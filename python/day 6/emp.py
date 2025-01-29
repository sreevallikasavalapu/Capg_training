class company1:
    def display(self,name):
        print("employees of company 1 are :")
        print(name)
    
class company2: 
    def display(self,name):
        print("employees of company 2 are :")
        print(name)
emp1=[]
emp2=[]
n=int(input("enter no of employees:"))
for i in range(n):
    print("please enter company 1 or 2: ")
    c=int(input())
    if(c==1):
        name=input("enter employee name: ")
        emp1.append(name)
    else:
        name=input("enter employee name: ")
        emp2.append(name)
c1=company1()
c2=company2()
c1.display(emp1)
c2.display(emp2)
