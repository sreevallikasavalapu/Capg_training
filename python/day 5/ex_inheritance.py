class Parent:
    def __init__(self):
        #self.bigNose=bigNose
        self.bigNose="7cm"
    def display_parent(self):
        print("This is the parent class.")
class Child(Parent):
    def __init__(self):
        super().__init__()
    def display_child(self):
        print("This is the child class.")
p=Parent()        
c=Child()
c.display_parent()
c.display_child() 
print(p.bigNose)
print(c.bigNose)