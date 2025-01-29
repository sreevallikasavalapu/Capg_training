def is_prime_v2(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    s=int(input())
    e=int(input())
    for i in range(s,e+1):
        if(is_prime_v2(i)):
            print(f"{i} is prime")
        
        # print(f"{i} is prime: {is_prime_v2(i)}")
main()

