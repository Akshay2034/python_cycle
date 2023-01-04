#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to 
#compare the area of 2 rectangles.

class ractangle:
    def __init__(self):
        self.__length=int(input("enter the lenghth of the rectangle"))
        self.__breadth=int(input("enter the breadth of the rectangle"))
    def __lt__(self,obj2):
        area=self.__length*self.__breadth
        area1=obj1.__length*obj2.__breadth
        print("area of rectangle1 is",area)
        print("area of rectangle2 is",area1)
        return area<area1
print("enter the length and breadth of first boject")
obj1=ractangle()
print("enter the length and breadth of second boject")
obj2=ractangle()
if obj1<obj2:
    print("rectangle1 is less than rectangle2")
else:
    print("rectangle1 is greater than rectangle2")