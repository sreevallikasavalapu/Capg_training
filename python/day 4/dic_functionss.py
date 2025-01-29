d={'apples':2,'banana':6,'papaya':1}

print(d.items())  #prints all the dictionary items

f=d.copy()        #copies dic values from one to another
print(f)

print(d.get('apples',0)) #retrieves keys pair item by taking key values

print(d.keys())         #prints all keys
print(d.values())       #prints all values
d.push({'grapes':3})
print(d.items())