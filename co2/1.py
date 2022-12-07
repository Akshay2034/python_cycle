#Program to find the factorial of a number 
# fact=1
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial of",n,"is:",fact)
def calc_fa(x):
    if x==1:
        return 1
    else:
        return(x*calc_fa(x-1))
num=int(input("enter a No"))
print("the factorial of",num,"is",calc_fa(num))