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
human = mwc.settinglist(human, 1)
carnivore = mwc.settinglist(carnivore, 2)
herbivore = mwc.settinglist(herbivore, 3)
grass = mwc.settinglist(grass, 4)
tree_nut = mwc.settinglist(tree_nut, 5)

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