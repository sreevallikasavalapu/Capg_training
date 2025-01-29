def display(max):     #function to display highest number
    print(f"highest number among three numbers is {max}")
def get_input_and_compare():       #function to get input
    a=input("enter 1st no: ")
    maxVariable="a"
    print(f"{maxVariable} is the biggest number")
    b=input("enter 2nd no: ")
    if b>maxVariable:
        maxVariable="b"
        print(f"{maxVariable} is the biggest number ")
    c=input("enter 3rd no: ")
    if c>maxVariable:
        maxVariable="c"
        print(f"{maxVariable} is the biggest number than {c}")
    return maxVariable
def main():
    maxi=get_input_and_compare()
    display(maxi)
main()
"""
another method
def display(max):     #function to display highest number
    print(f"highest number among three numbers is {max}")
ef get_input():
    a=input("enter 1st no: ")
    b=input("enter 2nd no: ")
    c=input("enter 3rd no: ")
    return (a,b,c)
def get_max(a,b,c):    #function to get maximum number 
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def main():
    max=get_input()
    display(max)
main()
    
"""