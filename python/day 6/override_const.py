class example:
    def _init_(self,name):   #first constructor will be overrided here
        print(f"first constructor name: {name}")
    def _init_(self,rno):    
        print(f"second constructor name: {rno}")
obj=example(87)              #goes to second constructor only