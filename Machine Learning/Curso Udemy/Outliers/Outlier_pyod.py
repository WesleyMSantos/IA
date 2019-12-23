# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:20:09 2019

@author: wesleysa
"""

import pandas as pd;

base = pd.read_csv('Curso Udemy/Base census e credit/credit-data.csv')

# Remover campos nulos
base = base.dropna()

import matplotlib.pyplot as plt
plt.boxplot(base.iloc[:, 2], showfliers=True)

from pyod.models.knn import KNN
detector = KNN()
detector.fit(base.iloc[:, 1:4])

# verifica os registros Outliers
previsoes = detector.labels_
confianca_previsoes = detector.decision_scores_


outliers = []
for i in range(len(previsoes)):
    #print(previsoes[i])
    if previsoes[i] == 1:
        outliers.append(i)

lista_outliers = base.iloc[outliers, :]

# Remover os Outliers
base = base.drop(lista_outliers.index)

base = base.drop_duplicates()

import matplotlib.pyplot as plt
plt.boxplot(base.iloc[:, 2], showfliers=True)