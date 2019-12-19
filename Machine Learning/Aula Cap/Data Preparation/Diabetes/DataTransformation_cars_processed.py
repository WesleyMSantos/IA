# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:10:19 2019

@author: wesleysa
"""

import pandas as pd

# CRIA UMA VARIAVEL QUE RECEBE OS DADOS DO ARQUIVO
base = pd.read_csv('Bases\cars_processed.csv')

# mostra os dados com o age menor que 0
base.loc[base['Age'] < 0]

# Verificar se cada coluna está com algum campo vazio
# Necessário mudar o nome da coluna
base.loc[pd.isnull(base['Age'])] # 2° FORMA(MELHOR)

# Transformation
from sklearn.preprocessing import LabelEncoder
labelencoder_base = LabelEncoder()

# transforma as informações da coluna Origin em números
base['Origin'] = labelencoder_base.fit_transform(base['Origin'])