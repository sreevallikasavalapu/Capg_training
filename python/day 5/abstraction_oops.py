class Employee:
    def __init__ (self,name,salary):
        self.__name=name
        self.__salary=salary
        
    def add_allowance(self,salary,bo,nf,all):
        return (self.__salary+bo+nf+all)
    
    def set_salary(self,salary):             #_protected single underscore
        self.__salary=salary                 #__private double underscore
    
    def deductions_cal(self,p,gst,ta,fa):
        k=p*(gst/100)
        return (p-k-ta-fa)
    
    def get_salary(self):
        return self.__salary
    
emp=Employee("Alice",5000)
print("salary before update : ",emp.get_salary())
sal=int(input("enter salary : "))
emp.set_salary(sal)
print("salary after update : ",emp.get_salary())
bo=int(input("enter bonus, night shifts, allowances : "))
nf=int(input()) 
all=int(input())
p=emp.add_allowance(sal,bo,nf,all)
print("total income after adding allowances : ",p)
gst=int(input("enter gst: "))
ta=int(input("enter traveling charges: "))
fa=int(input("enter food charges: "))
#emp.add_allowance(all)
q=emp.deductions_cal(p,gst,ta,fa)
print("total income : ",q)