'''n=int(input("enter the limit:"))
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
pypart(n)'''
n=int(input("enter the limit:"))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    print("\n")
for i in reversed(range(0,n+1)):
    for j in range(0,i):
        print("*",end="")
    print("\n")