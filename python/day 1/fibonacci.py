
def fib(n):
    if n<0:
        return -1
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input("enter number "))
print("fibonacci series is ")
for i in range(n):
    print(f"{fib(i)}")