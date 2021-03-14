import random
import matplotlib.pyplot as plt
import numpy as np

plt.xlim(0, 10)

class animal:#生物のクラス
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.life = 1
        self.food_want = 100
        self.speed = 0

    def migrate(self, goal_x, goal_y):#生物の移動関数
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

    def eat(self, prey, eatcounts):#生物の食事関数
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
    
    def action(self, humans, carnivores, herbivores, grasses, tree_nuts, eatcounts):#生物の行動関数
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
    
    def search_prey(self, prey, eatcounts):#生物の獲物探索関数
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

class human(animal):#親クラスanimalを継承した人間のクラス
    def __init__(self, id, x, y):
        super(human, self).__init__(id, x, y)
        self.relation = np.zeros(100)
        self.relation[id] = 0
        self.speed = random.randint(1, 3)


class carnivore(animal):#親クラスanimalを継承した肉食動物のクラス
    def __init__(self, id, x, y):
        super(carnivore, self).__init__(id, x, y)
        self.speed = random.randint(1, 3)
        self.strength = 100 - self.speed


class herbivore(animal):#親クラスanimalを継承した草食動物のクラス
    def __init__(self, id, x, y):
        super(herbivore, self).__init__(id, x, y)
        self.speed = random.randint(1, 3)
        self.strengh = 100 - self.speed


class plant:#植物のクラス
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.life = 1
    def rebirth(self):
        self.life = 1


class grass(plant):#親クラスplantを継承した雑草のクラス
    def __init__(self, id, x, y):
        super(grass, self).__init__(id, x, y)


class tree_nut(plant):#親クラスplantを継承した木の実のクラス
    def __init__(self, id, x, y):
        super(tree_nut, self).__init__(id, x, y)


def plot_all(humans, carnivores, herbivores, grasses, tree_nuts):#すべてのオブジェクトの描画関数
    plt.clf()
    plt.scatter(0, 0, c = "black")
    plt.scatter(0, 100, c = "black")
    plt.scatter(100, 0, c = "black")
    plt.scatter(100, 100, c = "black")
    for i in humans:
        if i.life == 1:
            plt.scatter(i.x, i.y, s = 5, c = "blue")
    for i in carnivores:
        if i.life == 1:
            plt.scatter(i.x, i.y, s = 5, c = "red")
    # for i in herbivores:
    #     if i.life == 1:
    #         plt.scatter(i.x, i.y, s = 5, c = "blue")
    # for i in grasses:
    #     if i.life == 1:
    #         plt.scatter(i.x, i.y, s = 5, c = "green")
    # for i in tree_nuts:
    #     if i.life == 1:
    #         plt.scatter(i.x, i.y, s = 5, c = "pink")
    plt.pause(0.1)

def generate_object(object, kind):
    if kind == 1:
        for i in range(10):
            object.append(human(i, random.randint(1, 100),random.randint(1, 100)))
        return object
    if kind == 2:
        for i in range(10):
            object.append(carnivore(i, random.randint(0,100), random.randint(0, 100)))
        return object
    if kind == 3:
        for i in range(10):
            object.append(herbivore(i, random.randint(0,100), random.randint(0, 100)))
        return object
    if kind == 4:
        for i in range(10):
            object.append(grass(i, random.randint(0,100), random.randint(0, 100)))
        return object
    if kind == 5:
        for i in range(10):
            object.append(tree_nut(i, random.randint(0, 100), random.randint(0, 100)))
        return object
