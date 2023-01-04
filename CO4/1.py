#Create Rectangle class with attributes length and breadth and methods to find area and perimeter.
#Compare two Rectangle objects by their area

class rectangle:
    def __init__(self):
        self.l=int(input("enter the length"))
        self.b=int(input("enter the breadth"))
    def get_area(self):
        return self.l*self.b
    
    def get_perimeter(self):
        return 2*self.l*self.b
    
    def compare(self,obj1):
        if obj.get_area()==obj1.get_area():
            print("botha are equal")
        elif obj.get_area() > obj1.get_area():
            print("area of first object greater than second object")
        else:
            print("area od second object greater than first object")      

print("enter the lenghth and breadth of the first object")
obj=rectangle()
print("enter the lenghth and breadth of the second object")
obj1=rectangle()

print("first area of rectangle",obj.get_area())
print("second area of rectangle",obj1.get_area())

print("first perimeter of first rectangle",obj.get_perimeter())
print("first perimeter of second rectangle",obj1.get_perimeter())

obj.compare(obj1)