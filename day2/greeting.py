import time

t=int(time.strftime('%H'))  #the time must be in int
print(t)

if(t>=0 and t<12):
    print("good morning")
elif(t>=12 and t<19):
    print("good afternoon")
else:
    print("good evening")