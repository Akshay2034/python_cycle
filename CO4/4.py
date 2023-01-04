#Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to 
#find sum of 2 time.

class time:
    def __init__(self):
        self.__h=int(input("enter the hour"))
        self.__m=int(input("enter the minutes"))
        self.__s=int(input("enter the seconds"))
    def __add__(self,t2):
        hours=self.__h+t2.__h
        print("sum of hours",hours)
        minutes=self.__m+t2.__m
        print("sum of minutes",minutes)
        seconds=self.__s+t2.__s
        print("sum of seconds",seconds)
        if minutes>60:
            hours+1
            minutes-=60
        if seconds>60:
            minutes+=1
            seconds-=60
        return(hours,minutes,seconds)
t1=time()
t2=time()
print("sum of h",obj1.hours)
print("sum of m",obj1.minutes)
print("sum of s",obj1.seconds)