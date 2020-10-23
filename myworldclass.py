import random
import matplotlib.pyplot as plt
import numpy as np


class creature:
    def __init__ (self, id, x, y):
        self.id = 0
        self.x = x
        self.y = y
        self.life = 1
    def migration (self, x, y):#migration
        self.x += x
        self.y += y
        if self.x > 100:
            self.x = 100
        elif self.x < 0:
            self.x = 0
        if self.y > 100:
            self.y = 100
        elif self.y < 0:
            self.y = 0

class human(creature):#human
    def __init__ (self, id, x, y):
        super(human, self).__init__(id, x, y)
        self.food_want = 0
        self.relation = np.zeros(100)
        self.relation[id] = 0
    def eat (self, animal):#eat
        self.food_want -= 80
        animal.life = 0

class canivore(creature):
    def __init__ (self, id, x, y):
        super(canivore, self).__init__(id, x, y)

class herbivore(creature):
    def __init__ (self, id, x, y):
        super(herbivore, self).__init__(id, x, y)


def plot_all (humanlist, animallist):
    plt.cla()
    for i in humanlist:
        plt.scatter(i.x, i.y, s=5, c="b")
    for i in animallist:
        plt.scatter(i.x, i.y, s=5, c="g")
    plt.pause(0.2)