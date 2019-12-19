# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:25:28 2019

@author: wesleysa
"""

import pandas as pd

base = pd.read_csv('census.csv')

# Transformação de variáveis categóricas
previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

# Transformação para dados numéricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # OneHot.. utilizado para variavés "Dummy"
labelencoder_previsores = LabelEncoder()
#labels = labelencoder_previsores.fit_transform(previsores[:,1])
#previsores[:, 0] = labelencoder_previsores.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[:, 6])
previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[:, 7])
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[:, 13])




# Na variavel previsores, cria uma tabela. 
# Para cada campo de uma coluna na base original, é criado uma coluna nova
onehotencoder = OneHotEncoder(categorical_features=[1, 3, 5, 6, 7, 8, 9, 13])
previsores = onehotencoder.fit_transform(previsores).toarray()


# Transformação da classe
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)