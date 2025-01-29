#empty dictionary
d={}
print(d)

#2 items in list
d={'eggs':'6','milk':'2'}
print(d)

#NESTING 
d={'fruits':{'apples':1,'banana':4}}
print(d)
print(d['fruits']['apples'])

#alternative constructive methods
d=dict(name='riya',age=21)
print(d)

#zipper pairs
keys_list=[1,2,3]
vals_list=[1001,1002,1003]
d=dict(zip(keys_list,vals_list))
print(d)

d=dict.fromkeys(['a','b'],[1,2])
print(d)

d={'colour':'green',
    'fruit':'grapes'}
print("pair of colour is ",d['colour'])