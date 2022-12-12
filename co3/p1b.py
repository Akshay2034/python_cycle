import time
print("current time in sec:",time.time())
print("current time:",time.ctime())
print("current time after 30 sec:",time.ctime(time.time()+30))
t=time.localtime()