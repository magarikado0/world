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
eatcount = np.zeros(8, dtype=np.int32)#0:hc 1:hb 2:ht 3:ch 4:cb 5:ct 6:bg 7:bt

count = 0
human = mwc.setlist(human, 1)
carnivore = mwc.setlist(carnivore, 2)
herbivore = mwc.setlist(herbivore, 3)
grass = mwc.setlist(grass, 4)
tree_nut = mwc.setlist(tree_nut, 5)

while(count < 50):
    mwc.plot_all(human, carnivore, herbivore, grass, tree_nut)
    for i in human:
        if i.life == 1:
            i.action(human, carnivore, herbivore, grass, tree_nut, eatcount)
    for i in carnivore:
        if i.life == 1:
            i.action(human, carnivore, herbivore, grass, tree_nut, eatcount)
    
    for i in herbivore:
        if i.life == 1:
            i.action(human, carnivore, herbivore, grass, tree_nut, eatcount)
    count += 1
print(eatcount)