def display(val): #displaying average of 4 numbers
    print(f"average of 4 numbers is {val}")
def get_input():
    a=input("enter 1st no: ")
    b=input("enter 2nd no: ")
    c=input("enter 3rd no: ")
    d=input("enter 4th no: ")
    n=input("enter avg no: ")
    return (a,b,c,d,n)
def get_sum(a,b,c,d):
    val=(int(a)+int(b)+int(c)+int(d))
    return val
def get_avg(val,n):
    data=int(val)/int(n)
    return data
def main():
    a,b,c,d,n=get_input()
    val=get_sum(a,b,c,d)
    data=get_avg(val,n)
    display(data)
main()