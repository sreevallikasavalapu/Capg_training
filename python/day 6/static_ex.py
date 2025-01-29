import dis
class Person:  
    def __init__(self, age):  
        self.age = age  
    def isAdult(age):  
        return age > 18
    
res = Person.isAdult(12) 
print('Is person adult:', res) 
res = Person.isAdult(22) 
print('\nIs person adult:', res) 
print(dis.dis(Person))
