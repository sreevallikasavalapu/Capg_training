
def palindrome_check(l2):
    return (l2==l2[::-1])

def space_reduce(l1):  #removing the extra spaces without using split method
    l2=[]
    for i in l1:
        if i==" ":
            continue
        else:
            l2.append(i)
    return l2

def main():
    str=input()
    l1=list(str)
    l2=space_reduce(l1)
    if(palindrome_check(l2)):
        print("list is palindrome, the list is",l2)
    else:
        print("not palindrome")
main() 
        