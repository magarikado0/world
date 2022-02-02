import matplotlib.pyplot as plt
import numpy as np
import random
 
np.random.seed(0)
 
class agent:
    def __init__(self, ability, parent_income):
        self.life = 1#60歳が全員の寿命
        self.ability = ability
        self.school = 2
        self.age = 0
        if parent_income == -1:#一世代目の生まれた時点での収入は乱数
            self.income = np.random.normal(2000, 500)
        else:
            self.income = parent_income#子供の所得は親の所得に単純に依存
    def profession_select(self):
        self.profession = self.ability#自分の能力が仕事のレベルになる
        self.income = self.profession#職業を選んだ時点で親の扶養から離れる
        self.school = 0#職業を選ぶ時点で学校は卒業
    def school_select(self):
        self.school = self.ability / 5#学校のレベルは自分の能力に比例
