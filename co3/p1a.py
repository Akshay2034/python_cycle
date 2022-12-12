import random
li=["ak","er","rt","tu","gj","dh","fg"]
print(random.choice(li))
print(random.choices(li,k=4))
print(random.sample(li,k=1))
random.shuffle(li)
print(random.randrange(2,7))