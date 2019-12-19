# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:04:07 2019

@author: wesleysa
"""

import pandas as pd

# CRIA UMA VARIAVEL QUE RECEBE OS DADOS DO ARQUIVO
base = pd.read_csv('Bases\diabetes_processed_incomplete.csv')

# mostra as informaçoes da tabela
base.describe()

# cria uma lista, pega os nomes da coluna da tabela e atribui a lista
nameColum = list()
for row in base:
    nameColum.append(row)

# exibe o nome das colunas    
for colum in nameColum:
    print(colum)

# Verifica qual coluna possui campos nulos 
# e imprime o nome da coluna que possui campo(s) nulos
indicesNulos = list() 

for i, lis in enumerate(nameColum):
    #print(f'Coluna {lis}: ')
    if pd.isnull(base[nameColum[i]]).any():
        indicesNulos.append(nameColum[i])
    #print(base.loc[pd.isnull(base[nameColum[i]])])
    #print()
print(indicesNulos) 

# mostrar o age que não foram preenchidos (null/blank)
base.loc[pd.isnull(base['Insulin'])] # 2° FORMA(MELHOR)


#Data Transformation
base['Insulin'].median() # MEDIANA DA IDADE

# calculando o valor mediano da coluna Insulin
mediana = base['Insulin'][base.Insulin > 0].median()


# 3 FORMAS PARA ATRIBUIR VALOR AOS CAMPOS NULL
# atribui o mediano para os campos NaN/null
base.update(base['Insulin'].fillna(mediana))

# atribui o mediano para os campos NaN/null
base.loc[pd.isnull(base.Insulin), 'Insulin'] = mediana

# atribui o mediano para os campos NaN/null
base['Insulin'].fillna(mediana, inplace = True) 

# 1 - apaga a coluna
base.drop('Age', 1, inplace=True)

            # SEPARAÇÃO DE CLASSES E PREVISORES
# PEGA TODAS AS COLUNAS DO 0 ATÉ O 6 (Coluna Age apagada)
previsores = base.iloc[:, 0:8].values 

# variavel armazena atributo de classe
classe = base.iloc[:, 8].values # PEGA A COLUNA 7 (Com coluna Age apagada)


# Escalonamento de atributos (deixar os atributos na mesma escala)

# Para que os algoritmos não dê preferência para os registros com os valores maiores
# Duas formas para fazer o escalonamento (Padronização (Standardisation) e Normalização (Normalization))

# Padronização
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# divisão da base de dados entre classe e previsores
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)




#Algortimo de treinamento Naive Bayes
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
# método fit, treinamento do algoritmo (gerar a tabela de probabilidade)
classificador.fit(previsores_treinamento, classe_treinamento)

# gera uma tabela com o resultado da probabilidade
previsoes = classificador.predict(previsores_teste)



# Algoritmo Árvore
from sklearn.tree import DecisionTreeClassifier
classificador = DecisionTreeClassifier(criterion='entropy', random_state=0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)



#Algoritmo Random Forest
from sklearn.ensemble import RandomForestClassifier
classificador = RandomForestClassifier(n_estimators=15, criterion='entropy', random_state=0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)


# Faz a compração do resultado da probabilidade com a resposta correta
# e apresenta a por centagem de acerto
from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)




