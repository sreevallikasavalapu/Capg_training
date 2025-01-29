def get_input():
    nums = [int(input(f"Enter number {i+1}:")) for i in range((int(input("Enter the size of nums:"))))]
    return nums

def check(nums):
    small = nums[0]
    big = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < small:
            small = nums[i]
        if nums[i] > big:
            big = nums[i]
    
    return small,big
def main():
    nums = get_input()
    a,b=check(nums)
    print("Smallest Number:", a)
    print("Biggest Number:", b)

main()