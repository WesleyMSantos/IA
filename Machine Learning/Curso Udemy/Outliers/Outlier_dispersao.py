# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:56:23 2019

@author: wesleysa
"""

import pandas as pd;

base = pd.read_csv('Curso Udemy/Base census e credit/credit-data.csv')

# Remover campos nulos
base = base.dropna()
base.loc[base.age < 0, 'age'] = 40.92

# Atribuindo a média para os valores menores que 0, da coluna age

# teste com par de variáveis
# income x age
import matplotlib.pyplot as plt
plt.scatter(base.iloc[:,1], base.iloc[:, 2])

# income x loan
plt.scatter(base.iloc[:,1], base.iloc[:, 3])

# age x loan
plt.scatter(base.iloc[:,2], base.iloc[:, 3])

base_census = pd.read_csv('Curso Udemy/Base census e credit/census.csv')

# age x final weight
plt.scatter(base_census.iloc[:, 0], base_census.iloc[:,2])