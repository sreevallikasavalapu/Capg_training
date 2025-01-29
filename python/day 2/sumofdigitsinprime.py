def check_prime(s):
    """if n>10000:
        return False
    elif n==2:
        return True
    else:
    """
        # while n>0:
            # s=s+(n%)
    n=0
    while s>0:
        n=n+(s%10)
        s=s//10
    
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
        return True
        
    return False
def main():
    n=int(input())
    if(check_prime(n)):
        print("it is prime number")
    else:
        print("is not prime number")
main()