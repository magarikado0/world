import random
import matplotlib.pyplot as plt
import numpy as np

class existance:
    def __init__(self, id, x, y):
        self.id = 0
        self.x = x
        self.y = y
        self.life = 1
        self.food_want = 100
    def migration(self, x, y):#migration
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

class human(existance):#human
    def __init__(self, id, x, y):
        super(human, self).__init__(id, x, y)
        self.relation = np.zeros(100)
        self.relation[id] = 0
    def eat (self, animal):#eat
        self.food_want -= 80
        animal.life = 0

class carnivore(existance):
    def __init__(self, id, x, y):
        super(carnivore, self).__init__(id, x, y)
    def eat(self, prey):
        self.food_want -=10
        prey.life = 0

class herbivore(existance):
    def __init__(self, id, x, y):
        super(herbivore, self).__init__(id, x, y)
    def eat(self, grass):
        grass.life = 0

class grass(existance):
    def __init__(self, id, x, y):
        super(grass, self).__init__(id, x, y)

def plot_all(human, carnivore, herbivore, grass):
    plt.cla()
    for i in human:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="brown")
    for i in carnivore:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="red")
    for i in herbivore:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="blue")
    for i in grass:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="green")
    plt.pause(0.2)