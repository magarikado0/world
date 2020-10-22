import random
import matplotlib.pyplot as plt
class human:#human
    def __init__ (self, id, x, y):
        self.id = id#id
        self.food_want = 0
        self.x = x
        self.y = y
        self.life = 1
        #self.energy=0
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
    def eat (self, animal):#eat
        self.food_want -= 80
        animal.life = 0
class animal:#animal
    def __init__ (self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.life = 1
def plot_all (humanlist, animallist):
    plt.cla()
    for i in humanlist:
        plt.scatter(i.x, i.y, s=5, c="b")
    for i in animallist:
        plt.scatter(i.x, i.y, s=5, c="g")
    plt.pause(0.2)