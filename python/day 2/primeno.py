import math
def is_prime_v2(n):
    if n <= 2:
        return False 
    if n > 10000:
        return True  
    else:
        #for i in range(2,int(n**(0.5))+1):  
        i=2
        while i<math.sqrt(n):#can be replaced in this line
            if(n%i==0):
                return False
            i+=1 
        return True
def main():
    s=int(input())
    e=int(input())
    for i in range(s,e+1):
        if(is_prime_v2(i)):
            print(f"{i} is prime")
        
        # print(f"{i} is prime: {is_prime_v2(i)}")
main()

"""
# Example usage:
number = 37
print(f"{number} is prime: {is_prime_v2(number)}")
"""