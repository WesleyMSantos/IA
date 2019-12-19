# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:20:30 2019

@author: wesleysa
"""

import pandas as pd
# CRIA UMA VARIAVEL QUE RECEBE OS DADOS DO ARQUIVO
# Arquivo original possui 590.540 linhas e 394 colunas
base = pd.read_csv('train_transaction.csv')


# cria uma lista, pega os nomes da coluna da tabela e atribui a lista
nameColum = list()
for row in base:
    nameColum.append(row)
    
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



# Colunas com campos nulos (sem as colunas D, M e V)
# card2', 'card3', 'card4'(Texto), 'card5', 'card6'(Texto), 'addr1', 'addr2', 
# 'dist1', 'dist2', 'P_emaildomain'(Texto), 'R_emaildomain'(Texto)

# calculando o valor mediano
medianaCard2 = base['card2'].median()
# atribui o mediano para os campos NaN/null
base['card2'].fillna(medianaCard2, inplace = True) 

medianaCard3 = base['card3'].median()
base['card3'].fillna(medianaCard3, inplace = True) 

medianaCard5 = base['card5'].median()
base['card5'].fillna(medianaCard5, inplace = True) 

medianaAddr1 = base['addr1'].median()
base['addr1'].fillna(medianaAddr1, inplace = True) 

medianaAddr2 = base['addr2'].median()
base['addr2'].fillna(medianaAddr2, inplace = True) 

medianaDist1 = base['dist1'].median() # resulta em 8
medianaDist1 = base['dist1'][base.dist1 > 0].median() # resulta em 10
base['dist1'].fillna(medianaDist1, inplace = True)

medianaDist2 = base['dist2'].median() # resulta 37
medianaDist2 = base['dist2'][base.dist2 > 0].median() # resulta em 61
base['dist2'].fillna(medianaDist2, inplace = True)



# apaga as linhas nulas (NaN)
base = base.dropna(subset=['card4'])

base = base.dropna(subset=['card6'])

# Realizar somente se não for excluir a coluna
base = base.dropna(subset=['P_emaildomain'])

# Verificar quantas linhas da coluna são nulas
base.loc[pd.isnull(base['isFraud'])]

# apaga a coluna
base.drop('TransactionID', 1, inplace=True)

base.drop('R_emaildomain', 1, inplace=True)


# Baixa correlação ***** (Testar) *****
base.drop('P_emaildomain', 1, inplace=True)



# Apagar colunas D, M e V (demora muito)
# Apagar as colunas D
for item in range (32,47):
    base.drop('D{}'.format(item), axis=1, inplace=True)

# Apaga as colunas M
for item in range (47,56):
    base.drop('D{}'.format(item), axis=1, inplace=True)

# Apagar as colunas V
for item in range (51,340):
    base.drop('V{}'.format(item), axis=1, inplace=True)
    
    

# Criando base sem as colunas D, M e V
baseSemD_M_V = base[base.columns[: -363]]



# Verificar os tipos de variações de letras
base.isFraud.value_counts()

# Pega os dados da coluna
baseSemD_M_V[baseSemD_M_V.columns[3]]



# Cria uma lista para transformação do texto para número
#Transformação ProductCD
a_trocar = {

    'W' : 1,
    'C' : 2,
    'R' : 3,
    'H' : 4,
    'S' : 5
}
baseSemD_M_V.ProductCD = baseSemD_M_V.ProductCD.map(a_trocar) 

# Tranformação do card4
a_trocar = {
    'discover': 1,
    'visa':2,
    'mastercard':3,
    'american express':4
}
baseSemD_M_V.card4 = baseSemD_M_V.card4.map(a_trocar) 

# Tranformação do card6
a_trocar = {
    'debit': 1,
    'credit':2,
    'debit or credit':3,
    'charge card':4
}
baseSemD_M_V.card6 = baseSemD_M_V.card6.map(a_trocar) 

# Transformação do P_emaildomain (Caso a coluna não tenha sido excluida) 
a_trocar = {
        
'gmail.com' : 1,
'yahoo.com' : 2,
'anonymous.com' : 3,
'aol.com' : 4,
'hotmail.com' : 5,
'comcast.net' : 6,
'icloud.com' : 7,
'att.net' : 8,
'msn.com' : 9,
'outlook.com' : 10,
'sbcglobal.net' : 11,
'verizon.net' : 12,
'live.com' : 13,
'ymail.com' : 14,
'bellsouth.net' : 15,
'me.com' : 16,
'cox.net' : 17,
'optonline.net' : 18,
'charter.net' : 19,
'rocketmail.com' : 20,
'mail.com' : 21,
'earthlink.net' : 22,
'mac.com' : 23,
'gmail' : 24,
'juno.com' : 25,
'aim.com' : 26,
'windstream.net' : 27,
'roadrunner.com' : 28,
'frontier.com' : 29,
'embarqmail.com' : 30,
'twc.com' : 31,
'netzero.com' : 32,  
'centurylink.net' : 33,
'netzero.net' : 34,
'frontiernet.net' : 35,
'q.com' : 36,
'suddenlink.net' : 37,
'cfl.rr.com' : 38,
'sc.rr.com' : 39,
'cableone.net' : 40,
'yahoo.com.mx' : 41,
'yahoo.es' : 42,
'protonmail.com' : 43,
'ptd.net' : 44,
'live.com.mx' : 45,
'outlook.es' : 46,
'yahoo.fr' : 47,
'hotmail.es' : 48,
'yahoo.co.uk' : 49,
'web.de' : 50,
'prodigy.net.mx' : 51,
'hotmail.fr' : 52,
'hotmail.co.uk' : 53,
'gmx.de' : 54,
'yahoo.de' : 55,
'live.fr' :  56,
'hotmail.de' :  57,
'servicios-ta.com' : 58, 
'yahoo.co.jp' :  59,
}
baseSemD_M_V.P_emaildomain = baseSemD_M_V.P_emaildomain.map(a_trocar) 
 


# Exportar DataFrma para arquivo .csv
baseSemD_M_V.to_csv('fraude_pre_processed.csv', index=False) 



# **** Verificar Outliers ***



# BALANCEAMENTO
# Pega 30000 dados com valor isFraud == 0
df_fraud0 = baseSemD_M_V[baseSemD_M_V.isFraud == 0].sample(40000)

df_fraud1 = baseSemD_M_V[baseSemD_M_V.isFraud == 1].sample(20000)

# Concatenado os dois DataFrames
frames = [df_fraud0, df_fraud1]
df_concat = pd.concat(frames)



# Separação de classe e previsores
previsores = df_concat.iloc[:, 1:28].values
classe = df_concat.iloc[:, 0].values 

# Exportar DataFrma para arquivo .csv
df_concat.to_csv('balance_fraude_pre_processed.csv', index=False) 


# Escalonamento dos valores
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)



# Classificador Random Forest
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classificador = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)



# Classificador LinearSVC
import numpy as np
train = pd.read_csv('balance_fraude_pre_processed.csv')
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
train_x, test_x, train_y, test_y = train_test_split(train.drop('isFraud', axis = 1), train['isFraud'])
clf = LinearSVC()
clf.fit(train_x, train_y)
round(accuracy_score(test_y, clf.predict(test_x)) * 100, 1)






