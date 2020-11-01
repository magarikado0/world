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
human = mwc.setlist(human, 1)
carnivore = mwc.setlist(carnivore, 2)
herbivore = mwc.setlist(herbivore, 3)
grass = mwc.setlist(grass, 4)
tree_nut = mwc.setlist(tree_nut, 5)

while(count<100):
    mwc.plot_all(human, carnivore, herbivore, grass, tree_nut)
    for i in human:
        i.action(human, carnivore, herbivore, grass, tree_nut)
    for i in carnivore:
        i.action(human, carnivore, herbivore, grass, tree_nut)
    for i in herbivore:
        i.action(human, carnivore, herbivore, grass, tree_nut)
    count += 1