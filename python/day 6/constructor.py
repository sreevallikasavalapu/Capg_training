class csm:
    def display(self,val,name):
        print(f"name: {name} , department :CSM , marks: {val} ")
class cse:
    def display(self,val,name):
        print(f"name: {name} , department :CSE , marks: {val} ")
for veh in [csm(),cse()]:
    name=input("enter name: ")
    n=int(input("enter marks: "))
    veh.display(n,name)    
    