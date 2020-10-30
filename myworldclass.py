import random
import matplotlib.pyplot as plt
import numpy as np

class animal:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.life = 1
        self.food_want = 100
    def migration(self, goal_x, goal_y):#migration
        if goal_x - self.x > 0:
            self.x += self.speed
        elif goal_x - self.x < 0:
            self.x -= self.speed
        if goal_y - self.y > 0:
            self.y += self.speed
        elif goal_y - self.y < 0:
            self.y -= self.speed
        if self.x > 100:
            self.x = 100
        elif self.x < 0:
            self.x = 0
        if self.y > 100:
            self.y = 100
        elif self.y < 0:
            self.y = 0
    def eat(self, prey):
        prey.life = 0
        if type(prey) == grass:
            self.food_want -= 10
        elif type(prey) == tree_nut:
            self.food_want -= 20
        elif type(prey) == carnivore:
            self.food_want -= 30
        else:
            self.food_want -= 20

class human(animal):#human
    def __init__(self, id, x, y):
        super(human, self).__init__(id, x, y)
        self.relation = np.zeros(100)
        self.relation[id] = 0
        self.speed = random.randint(1, 3)

class carnivore(animal):
    def __init__(self, id, x, y):
        super(carnivore, self).__init__(id, x, y)
        self.speed = random.randint(1, 3)
        self.strength = 100 - self.speed

class herbivore(animal):
    def __init__(self, id, x, y):
        super(herbivore, self).__init__(id, x, y)
        self.speed = random.randint(1, 3)
        self.strengh = 100 - self.speed


class plant:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.life = 1
    def rebirth(self):
        self.life = 1

class grass(plant):
    def __init__(self, id, x, y):
        super(grass, self).__init__(id, x, y)

class tree_nut(plant):
    def __init__(self, id, x, y):
        super(tree_nut, self).__init__(id, x, y)


def plot_all(humans, carnivores, herbivores, grasses, tree_nuts):
    plt.clf()
    for i in humans:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="brown")
    for i in carnivores:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="red")
    for i in herbivores:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="blue")
    for i in grasses:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="green")
    for i in tree_nuts:
        if i.life == 1:
            plt.scatter(i.x, i.y, s=5, c="pink")
    plt.pause(0.5)
