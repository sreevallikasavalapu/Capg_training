#import array can also be used

#empty list
l1=[]
print("empty list is ",l1)

#a list of 4 numbers (index 0 to 3)
l2=[1,2,3,4]
print("elements of list are : ",l2)

# nested list
l3=['a',['b','c']]
print("nested list is : ",l3)

#creating a list from string 
l4=list('hello')
print("list created from string hello is : ",l4)

#creating a list with range
l5=list(range(-2,2)) #prints from -2 to 1
print("range of  numbers are : ",l5)

#Accessing an element by index 
l6=[10,20,30,40]
print("elements at index 2 is :",l6[2])

#accessing an element from nested list by index
l7=['x',[10,20,30],'y']
print("element at l7[1][2] : ",l7[1][2])

#slicing a list
l8=[0,1,2,3,4,5]
print("slicing l8 from index 2 to 4 (l8[2:5]): ",l8[2:5])

#getting length of a list
print("length of l8 is ",len(l8))

#demonstrating nested indexing and slicing together
l9=[10,[100,200,300,400,],50]
print("element at l9[1]:",l9[1])   #access the sublist
print("element at l9[1][3]: ",l9[1][3]) #access element 3 from the sublist
print("slicing sublist l9[1][1:3]: ",l9[1][1:3])  #slice the sublist

#summary of outputs
print("\n summary of lists: ")
print("l1:", l1)
print("l2:", l2)
print("l3:", l3)
print("l4:", l4)
print("l5:", l5)
print("l6:", l6)
print("l7:", l7)
print("l8:", l8)
print("l9:", l9)

