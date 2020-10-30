import myworldclass as mwc
import random
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
plt.xlim([0,100])
plt.ylim([0,100])

human = []
carnivore= []
herbivore = []
grass = []
tree_nut = []
dis_min = 20000
min_index = 0

count = 0

for i in range(10):
    human.append(mwc.human(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    carnivore.append(mwc.carnivore(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    herbivore.append(mwc.herbivore(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    grass.append(mwc.grass(i, random.randint(0,100), random.randint(0, 100)))

for i in range(10):
    tree_nut.append(mwc.tree_nut(i, random.randint(0, 100), random.randint(0, 100)))
    
while(count<100):
    mwc.plot_all(human, carnivore, herbivore, grass, tree_nut)
    for i in human:
        for index, k in enumerate(carnivore):
            if k.life == 1:
                dis = (i.x - k.x)**2 + (i.y - k.y)**2
                if dis < dis_min:
                    dis_min = dis
                    min_index = index
        #print(dis_min)
        if dis_min <= 9:
            i.eat(carnivore[min_index])
        elif dis_min <= 100:
            i.migration(carnivore[min_index].x, carnivore[min_index].y)
        else:
            i.migration(random.randint(0,100),random.randint(0,100))
        dis_min = 20000
    count += 1