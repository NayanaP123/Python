l=[1,2,3,"nayana"]
print(l)
print(type(l))  #type
print(l[0])   #index
print(l[-1])   #last index
print(len(l))


#if
if 3 in l:
    print("yes")
else:
    print("no")


#return whole list
print(l[:])


#slicing
print(l[1:-1])
print(l[0:4])


#increment/difference by 2
print(l[1:-1:2])




#another way to take list
l=[i for i in range(4)]
print(l)



l=[i*i for i in range(4)]
print(l)

l=[i for i in range(4) if i%2==0]
print(l)