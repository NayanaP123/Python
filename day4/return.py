def avg(*numbers): 
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)   #c   -----also declare it in call and then print it

c=avg(1,2,3,4)
print(c)
