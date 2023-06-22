t=(1,2,3)
print(type(t),t)

#multiple items in single variable



print(t[1])  #inddexing (+ve and -ve indexing)
print(t[1:3])#slicing
print(len(t)) #length


if 3 in t:
    print("yes")

#tuples are immutable
#tuple operations
temp=list(t)   #---to convert tuple to list, so, that we can change items
print(temp)

temp.append("nayana")  # to add
print(temp)

temp.pop(2)   #----to delete
print(temp)


temp[2]="hi"     #insert at particular point
print(temp)

t=tuple(temp)  #list to tuple
print(t)


c=temp.count(1)  #to count
print(c)


c=temp.index(1)   #to find index
print(c)


c=len(temp)  #length
print(c)