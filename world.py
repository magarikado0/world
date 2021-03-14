import myworldclass as mwc
import random
import matplotlib.pyplot as plt
import numpy as np

human = []
carnivore= []
herbivore = []
grass = []
tree_nut = []
eatcount = np.zeros(8, dtype=np.int8)#0:hc 1:hb 2:ht 3:ch 4:cb 5:ct 6:bg 7:bt

count = 0
human = mwc.generate_object(human, 1)
carnivore = mwc.generate_object(carnivore, 2)
# herbivore = mwc.generate_object(herbivore, 3)
# grass = mwc.generate_object(grass, 4)
# tree_nut = mwc.generate_object(tree_nut, 5)

while(count < 50):
    mwc.plot_all(human, carnivore, herbivore, grass, tree_nut)
    for i in human:
        if i.life == 1:
            i.action(human, carnivore, herbivore, grass, tree_nut, eatcount)
    for i in carnivore:
        if i.life == 1:
            i.action(human, carnivore, herbivore, grass, tree_nut, eatcount)
    # for i in herbivore:
    #     if i.life == 1:
    #         i.action(human, carnivore, herbivore, grass, tree_nut, eatcount)
    count += 1
print(eatcount)
