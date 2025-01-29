from math import inf
def main():  
    list1=[]
    n=int(input("enter size: "))
    print("enter elements: ")
    max,min=-inf,inf
    for i in range(n):
        x=int(input())
        if x>max:
            max=x
        if x<min:
            min=x
        list1.append(x)
    print("sum is ",sum(list1))
    print("max element is ",max)
    print("min element is ",min)
main()