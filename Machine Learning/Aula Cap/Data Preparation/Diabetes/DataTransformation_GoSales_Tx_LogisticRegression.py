# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:35:16 2019

@author: wesleysa
"""

import pandas as pd

# CRIA UMA VARIAVEL QUE RECEBE OS DADOS DO ARQUIVO
base = pd.read_csv('Bases\GoSales_Tx_LogisticRegression.csv')

# mostra os dados com o age menor que 0
base.loc[base['AGE'] < 0]

# Verificação de valores nulos
base.loc[pd.isnull(base['PROFESSION'])] # 2° FORMA(MELHOR)


# Transformação de variáveis categóricas
previsores = base.iloc[:, 0:2].values

# Transformação para dados numéricos
from sklearn.preprocessing import LabelEncoder
labelencoder_previsores = LabelEncoder()

# Transformação feita atribuindo para outra variável
labels = labelencoder_previsores.fit_transform(previsores[:,0])

#Transformação direto na base
base['IS_TENT'] = labelencoder_previsores.fit_transform(base['IS_TENT'])
base['GENDER'] = labelencoder_previsores.fit_transform(base['GENDER'])
base['MARITAL_STATUS'] = labelencoder_previsores.fit_transform(base['MARITAL_STATUS'])
base['PROFESSION'] = labelencoder_previsores.fit_transform(base['PROFESSION'])
