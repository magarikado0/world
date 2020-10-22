import myworldclass as mwc
import random
import matplotlib.pyplot as plt
import time
plt.xlim([0,100])
plt.ylim([0,100])
all_human=[]
all_animal=[]
count=0
fig=plt.figure()
for i in range(100):
    all_human.append(mwc.human(i,random.randint(0,100),random.randint(0,100)))
for i in range(50):
    all_animal.append(mwc.animal(i,random.randint(0,100),random.randint(0,100)))
while(count<10):
    mwc.plot_all(all_human,all_animal)
    for i in all_human:
        i.migration(1,1)
    time.sleep(0.6)
    count+=1