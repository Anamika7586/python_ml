n = int(input("Enter a number:"))
if (n%2 != 0):
    print("Weird")
else:
    if(n >= 2 and n <=5):
        print("Not weird")
    elif(n >=6 and n <= 20):
        print("weird")
    elif(n>20):
        print("Not Weird")


