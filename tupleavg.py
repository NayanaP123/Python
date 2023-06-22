def avg(*numbers): # to get all numbers from the tuple
    sum=0
    for i in numbers:
        sum=sum+i
    print("avg= ",sum/len(numbers))

avg(1,2,3,4)



