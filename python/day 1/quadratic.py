import cmath
n=input("enter quadratic expression")
a=int(input(""))
b=int(input(""))
c=int(input(""))
r1=(-b+cmath.sqrt(b*b - 4*a*c))/2*a
r2=(-b-cmath.sqrt(b*b - 4*a*c))/2*a
print(r1,r2)