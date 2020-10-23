import myworldclass as mwc
import random
import matplotlib.pyplot as plt

fig = plt.figure()
plt.xlim([0,100])
plt.ylim([0,100])

human = []
carnivore= []
herbivore = []
grass = []

count = 0

for i in range(10):
    human.append(mwc.human(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    carnivore.append(mwc.carnivore(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    herbivore.append(mwc.herbivore(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    grass.append(mwc.grass(i, random.randint(0,100), random.randint(0, 100)))
    
while(count<10):
    mwc.plot_all(human, carnivore, herbivore, grass)
    for i in human:
        i.migration(1, 1)
    count += 1
