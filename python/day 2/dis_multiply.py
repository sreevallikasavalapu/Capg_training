#dis assemble program
import dis
def multiply():
    a=1
    b=2
    c=int(a)*int(b)
    return c
def fun1():
    i,sum=0,0
    for i in range(4):
        sum=i+sum
    return sum
def add():
    a=4
    b=3
    c=int(a)+int(b)
    return c
def sub():
    a=4
    b=3
    c=int(a)-int(b)
    return c
def main():
    c=multiply()
    #for i in range(4):
    # dis.dis(sub)
    # dis.dis(add)
    # dis.dis(multiply)
    dis.dis(fun1)
main()