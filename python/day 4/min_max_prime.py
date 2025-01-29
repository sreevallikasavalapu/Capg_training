from math import inf
l1=[]
def check_prime(n):
    if n < 2:  
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True
"""def check_max_min():
    max,min=-inf,inf
    for i in l1:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min """       
def main():
    while True:
        start = int(input("Enter the start of the range (a): "))
        end = int(input("Enter the end of the range (b): "))
        
        if start < 1 or end < 1 or end > 10000 or start > end:
            print("Invalid input. Please enter valid numbers within the range (1 <= a <= b <= 10000).")
            continue
        
        print(f"Prime numbers between {start} and {end} are:")
        for i in range(start, end + 1):
            if check_prime(i):
                l1.append(i)
                print(i, end=" ")
        print()
        #max,min=check_max_min()  
        print("max value is ",l1[0])
        print("min value is ",l1[len(l1)-1])
        break 

main()
