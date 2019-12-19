# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
# Tratamento de valores inconsistentes

# IMPORTA O PANDAS E CRIA UM APELIDO PD
import pandas as pd

# CRIA UMA VARIAVEL QUE RECEBE OS DADOS DO ARQUIVO
base = pd.read_csv('credit-data.csv')

# mostra as informaçoes da tabela
base.describe()

# mostra os dados com o age menor que 0
base.loc[base['age'] < 0]

# formas de tratar os registros

# 1 - apaga a coluna
base.drop('age', 1, inplace=True)

# 2 - apagar somente registros com problemas (age menor que 0)
base.drop(base[base.age < 0].index, inplace=True)

# 3 - preencher os valores manualmente

# 4 - preencher os valores com a média (forma mais interessante)
base.mean() # MEDIA DE TODOS OS CAMPOS
base['age'].mean() # MEDIA DA IDADE

# pegar média somente das pessoas que a idade é maior que 0
base['age'][base.age > 0].mean()

# atualiza o age menor que 0 com a média
base.loc[base.age < 0, 'age'] = 40.92





# Tratamento de valores faltantes

# duas formas para mostrar o age que não foram preenchidos (null/blank)
pd.isnull(base['age']) # 1° FORMA DE VERIFICAR
base.loc[pd.isnull(base['age'])] # 2° FORMA(MELHOR)

# Necessário realizar divisão no data frame (base de dados)
# dos atributos previsores e atributos classe

# variavel armazena os atributos previsores (colunas income, age e loan)
previsores = base.iloc[:, 1:4].values # PEGA TODAS AS LINHAS, DA COLUNA 1 ATÉ A 4-1

# variavel armazena atributo de classe
classe = base.iloc[:, 4].values # PEGA TODAS AS LINHAS, DA COLUNA 4

# Atualiza os registros que estão em brancos (NaN) com a média
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])





# Escalonamento de atributos (deixar os atributos na mesma escala)

# Para que os algoritmos não dê preferência para os registros com os valores maiores
# Duas formas para fazer o escalonamento (Padronização (Standardisation) e Normalização (Normalization))

# Padronização
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)






