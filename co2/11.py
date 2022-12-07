l=int(input("enter lengeth of rectangle:"))
b=int(input("enter breadth of rectangle:"))
h=int(input("enter hieght of traingle:"))
ar=lambda x,y:x*y
asq=lambda x:x*x
at=lambda x,y:0.5*x*y
print("area if resctangle:",ar(l,b))
print("area if square:",asq(l))
print("area if triangle:",at(b,h))