#Patterns *

n = int(input("Enter Rows : "))
#n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("")