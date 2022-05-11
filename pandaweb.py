# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:17:30 2021

@author: Karina
"""

import pandas as pd


states = []
dict_scf = {}
    
dfs = pd.read_html('https://www.ipl.org/div/stateknow/chart.html',header=0)
for df in dfs:
    a = df.values.tolist()
    #print(a)

for i in range(0, len(a)):
    state = a[i][0]
    states.append(state)
    capital = a[i][1]
    flower = a[i][4]
    dict_scf[state] = (capital, flower)
    
print(dict_scf)

print()
print('Tennessee from dict')
print(dict_scf.get('Tennessee'))

c, f = dict_scf.get('Tennessee')
print("c = ", c)

#population from https://worldpopulationreview.com/states/state-capitals

dfs = pd.read_html('https://worldpopulationreview.com/states/state-capitals',header=0)
for df in dfs:
    p = df.values.tolist()

popul_dict = {}

for i in range(0, len(p)):
    state_p = p[i][1]
    populat = p[i][2]
    popul_dict[state_p] = populat
    
print(popul_dict)
print('Minnesota = ', popul_dict.get('Minnesota'))

print(len(p), '  len p')
print(len(states), '  len states')