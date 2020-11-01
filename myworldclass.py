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

    def migrate(self, goal_x, goal_y):#migration
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
        if self.food_want <= 95:
            self.food_want += 5

    def eat(self, prey, eatcounts):
        prey.life = 0
        if type(prey) == grass:
            self.food_want -= 10
            eatcounts[6] += 1
        elif type(prey) == tree_nut:
            self.food_want -= 20
            if type(self) == human:
                eatcounts[2] += 1
            elif type(self) == carnivore:
                eatcounts[5] += 1
            else:
                eatcounts[7] +=1
        elif type(prey) == carnivore:
            self.food_want -= 40
            eatcounts[0] += 1
        elif type(prey) == human:
            #self.food_want -= 30
            eatcounts[3] += 1
        else:
            self.food_want -= 30
            if type(self) == human:
                eatcounts[1] += 1
            elif type(self) == carnivore:
                eatcounts[4] += 1
    
    def action(self, humans, carnivores, herbivores, grasses, tree_nuts, eatcounts):
        if self.food_want >= 70:
            if type(self) == human:
                self.search_prey(carnivores, eatcounts)
            elif type(self) == carnivore:
                self.search_prey(humans, eatcounts)
            elif type(self) == herbivore:
                self.search_prey(tree_nuts, eatcounts)
        elif self.food_want >= 40:
            if type(self) == human:
                self.search_prey(herbivores, eatcounts)
            elif type(self) == carnivore:
                self.search_prey(herbivores, eatcounts)
            elif type(self) == herbivore:
                self.search_prey(grasses, eatcounts)
        elif self.food_want >=10:
            if type(self) == human:
                self.search_prey(tree_nuts, eatcounts)
            elif type(self) == carnivore:
                self.search_prey(tree_nuts, eatcounts)
            elif type(self) == herbivore:
                self.search_prey(grasses, eatcounts)
    
    def search_prey(self, prey, eatcounts):
        dis_min = 200000
        min_index = 0
        for index, k in enumerate(prey):
            if k.life == 1:
                dis = (self.x - k.x)**2 + (self.y - k.y)**2
                if dis < dis_min:
                    dis_min =dis
                    min_index = index
        if dis_min <=9:
            self.eat(prey[min_index], eatcounts)
        elif dis_min <= 100:
            self.migrate(prey[min_index].x, prey[min_index].y)
        else:
            self.migrate(random.randint(0, 100), random.randint(0,100))

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
            plt.scatter(i.x, i.y, s=5, c="black")
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
    plt.pause(0.1)


def setlist(exist, kind):
    if kind == 1:
        for i in range(10):
            exist.append(human(i, random.randint(1, 100),random.randint(1, 100)))
        return exist
    if kind == 2:
        for i in range(10):
            exist.append(carnivore(i, random.randint(0,100), random.randint(0, 100)))
        return exist
    if kind == 3:
        for i in range(10):
            exist.append(herbivore(i, random.randint(0,100), random.randint(0, 100)))
        return exist
    if kind == 4:
        for i in range(10):
            exist.append(grass(i, random.randint(0,100), random.randint(0, 100)))
        return exist
    if kind == 5:
        for i in range(10):
            exist.append(tree_nut(i, random.randint(0, 100), random.randint(0, 100)))
        return exist