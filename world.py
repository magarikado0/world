import myworldclass as mwc
import random
import matplotlib.pyplot as plt
import time
plt.xlim([0,100])
plt.ylim([0,100])
human = []
herbivore = []
count = 0
fig = plt.figure()
for i in range(100):
    human.append(mwc.human(i, random.randint(0,100), random.randint(0, 100)))
for i in range(50):
    herbivore.append(mwc.herbivore(i, random.randint(0,100), random.randint(0, 100)))
while(count<10):
    mwc.plot_all(human, herbivore)
    for i in human:
        i.migration(1, 1)
    time.sleep(0.5)
    count += 1
