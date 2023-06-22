a="nayana!!"
print(len(a))
print(a.upper())

# strings are immutable

print(a.lower())
print(a.rstrip("!"))  #rstrip("")  removes object
print(a.replace("ya","N"))  #replace
print(a.split(" "))    #split word between space

print(a.capitalize())   #capitalize first letter of each word

print(a.center(50))  #align to center
print(len(a.center(50)))


print(a.endswith("!!"))   #checks T/F

print(a.count("a"))  #count
print(a.find("a"))   #get indeex value of first appearance, if it is not present then it returns -1
print(a.isalnum())  #check A-Z,a-z,0-9
print(a.isalpha())  #check A-Z,a-z
print(a.islower())  #true if it contains small letters only
print(a.isprintable())  #check printable.\,eliminate \n
print(a.isspace())#check space
print(a.istitle())# check title capitalize
print(a.startswith("n")) #check
print(a.swapcase())#change case
print(a.title())#capitalize first letter of each word in paragraph






