#match is "switch"

x=int(input("X="))
match x:
    case 0:
        print("Zero")
    case 1:
        print("four")
    
    case _ if(x!=10):
        print(x,"is not 10")

    case _:  #default value
        print(x)