# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:29:27 2019

@author: wesleysa
"""

import pandas as pd;

base = pd.read_csv('Curso Udemy/Base census e credit/credit-data.csv')

# Remover campos nulos
base = base.dropna()

# outliers idade
import matplotlib.pyplot as plt
plt.boxplot(base.iloc[:, 2], showfliers=True)
outliers_age = base[(base.age < -20)]

plt.boxplot(base.iloc[:, 3])
outliers_loan = base[(base.loan > 13400)]