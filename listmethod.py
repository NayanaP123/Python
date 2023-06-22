l=[1,2,3]
print(l)


l.append(5)
print(l)     #add


l.sort(reverse=True)
print(l)         #reverse

print(l.index(1))  #get word from index

print(l.count(3))   #count a character

m=l    #add/insert a element
m[0]=0
print(l)


l.insert(1,3444)   #insert
print(l)

m=[100,2000]
l.extend(m)
print(l)     #add at end / concatenate



m=[1,1,2,3]
k=l+m
print(l)


