'''num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)'''
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter fisrt number:"))
b=int(input("enter second number:"))
GCD=gcd(a,b)
print("GCD is:")
print(GCD)