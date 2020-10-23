import myworldclass as mwc
import random
import matplotlib.pyplot as plt
import time

fig = plt.figure()
plt.xlim([0,100])
plt.ylim([0,100])

human = []
carnivore= []
herbivore = []
grass = []

count = 0

for i in range(100):
    human.append(mwc.human(i, random.randint(0,100), random.randint(0, 100)))

for i in range(50):
    carnivore.append(mwc.carnivore(i, random.randint(0,100), random.randint(0, 100)))

for i in range(50):
    herbivore.append(mwc.herbivore(i, random.randint(0,100), random.randint(0, 100)))

for i in range(50):
    grass.append(mwc.grass(i, random.randint(0,100), random.randint(0, 100)))
    
while(count<10):
    mwc.plot_all(human, carnivore, herbivore, grass)
    for i in human:
        i.migration(1, 1)
    time.sleep(0.5)
    count += 1
