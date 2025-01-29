def palindrome_check(l1):
    return (l1==l1[::-1])
    # k=int(n/2)
    # for i in range(k):
    #     if l1[i]!=l1[n-1]:
    #         return False
    # return True
def main():
    str=input()
    l1=list(str)
    #n=len(l1)
    if(palindrome_check(l1)):
        print("list is palindrome, the list is",l1)
    else:
        print("not palindrome")
    # print(l1)
main()