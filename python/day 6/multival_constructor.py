class example:
    def _init_(self,*args):   #'*' is used for taking multiple inputs in the constructor
        if len(args)==1:
            print(f"hello {args[0]}")
        elif len(args)==2:
            print(f"hello {args[0]}, you are {args[1]} years old.")
obj1=example("alice")
obj2=example("bob",25)