import numpy as np
import subject_society as sbs
import ideal_society as ids
import matplotlib.pyplot as plt
 
def gini(a):#ジニ係数を求める関数
    a.sort()
    n = len(a)
    num = 0
    for i in range(n):
        num = num + (i + 1) * a[i]
    deno = n * sum(a)
    return ((2 * num) / deno - (n + 1) / (n)) * (n / (n - 1))
 
income1 = []
income2 = []
agents1 = []
agents2 = []
 
ability_list = np.random.normal(2000, 500, 30000)#最初に人間を用意して、それらの人々を調査対象社会と理想社会のそれぞれでシミュレーションする
 
for i in range(1000):
    agents1.append(sbs.agent(ability_list[i], -1))
 
time_count = 0
population = 1000
 
while(time_count < 1000):
    for i in agents1:
        i.age += 1
        i.ability += i.school
        if i.age == 11:#11歳で能力と経済力に応じて学校を選ぶ
            i.school_select()
        if i.age == 21 and i.school != 0:#21歳で能力に応じて職業を選ぶ
            i.profession_select()
        if i.age == 35:#35歳で子供を産む
            agents1.append(sbs.agent(ability_list[population], i.income))
            population += 1
        if i.age == 60:#60歳が寿命
            i.life = 0
    time_count += 1
 
for i in agents1:
    income1.append(i.income)#調査対象社会における人々の収入を保存
 
for i in range(1000):
    agents2.append(ids.agent(ability_list[i], -1))
 
time_count = 0
population = 1000
 
while(time_count < 1000):
    for i in agents2:
        i.age += 1
        i.ability += i.school
        if i.age == 11:#11歳で能力と経済力に応じて学校を選ぶ
            i.school_select()
        if i.age == 21 and i.school != 0:#21歳で能力に応じて職業を選ぶ
            i.profession_select()
        if i.age == 35:#35歳で子供を産む
            agents2.append(ids.agent(ability_list[population], i.income))
            population += 1
        if i.age == 60:#60歳が寿命
            i.life = 0
    time_count += 1
 
 
for i in agents2:
    income2.append(i.income)#理想社会における人間の収入を保存
 
mean1 = np.mean(income1)#調査対象社会における平均所得
mean2 = np.mean(income2)#理想における平均所得
gini1 = gini(income1)#調査対象社会におけるジニ係数
gini2 = gini(income2)#理想社会におけるジニ係数
 
P = 0
for (i, j) in zip(income1, income2):#『親ガチャ度』の計算
    value1 = i / mean1
    value2 = j / mean2
    P += max(value2 - value1, 0)
 
plt.figure(0)
plt.hist(income1, bins = 50)
plt.figure(1)
plt.hist(income2, bins = 50)
plt.show()
print("親ガチャ度" + str(P))
print("調査対象社会のジニ係数" + str(gini1))
print("理想社会のジニ係数" + str(gini2))
