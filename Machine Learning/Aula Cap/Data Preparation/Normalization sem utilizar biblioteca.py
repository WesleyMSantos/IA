# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:19:49 2019

@author: wesleysa
"""

import pandas as pd

base = pd.read_csv('Curso Udemy/Base census e credit/census.csv')

# Normalizaçao (Normalization) sem utilizar biblioteca. Somente uma coluna
valorMax = base['age'].max()
valorMin = base['age'].min()

for i in base.index:
    base.loc[i, 'age'] = (base.loc[i, 'age'] - valorMin) / (valorMax - valorMin)



# Outra forma de Normalização, com todas as colunas
    
# cria uma lista que pega os nomes da coluna do data frame e atribui a lista
nameColum = list()
for row in base:
    nameColum.append(row)
    
# Primeiro for pega o nome da coluna. 
# Segundo for faz o calculo e atribui o valor para cada campo.
for j, lis in enumerate(nameColum):
    valorMax = base[f'{lis}'].max()
    valorMin = base[f'{lis}'].min()
    for i in base.index:
        base.loc[i, f'{lis}'] = (base.loc[i, f'{lis}'] - valorMin) / (valorMax - valorMin)

