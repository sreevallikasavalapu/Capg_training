class Parent:
    def display_parent(self):
        print("This is the parent class.")
class Child(Parent):
    def display_child(self):
        print("This is the child class.")
c=Child()
c.display_parent()
c.display_child() 