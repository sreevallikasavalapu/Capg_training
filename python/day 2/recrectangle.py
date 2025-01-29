def display(data):
    print(f"the area is {data}")
def get_input():
    length=input("length: ")
    width=input("width: ")
    return length,width
def compute_area(length,width):
    area=int(length)*int(width)
    return area
def main():
    length,width=get_input()
    data=compute_area(length,width)
    display(data)
main()
