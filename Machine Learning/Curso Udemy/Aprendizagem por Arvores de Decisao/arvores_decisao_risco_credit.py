# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:22:06 2019

@author: wesleysa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:36:39 2017

@author: Jones
"""
import pandas as pd

base = pd.read_csv('risco-credito.csv')
previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values
                  
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
                 
from sklearn.tree import DecisionTreeClassifier, export
classificador = DecisionTreeClassifier(criterion='entropy')

# método fit, treinamento do algoritmo (gerar a tabela de probabilidade)
classificador.fit(previsores, classe)
print(classificador.feature_importances_)

# visualização da árvore
export.export_graphviz(classificador,
                       out_file= 'arvore.dot',
                       feature_names= ['historia', 'divida', 'garantias', 'renda'], 
                       class_names= ['alto', 'moderado', 'baixo'],
                       filled= True,
                       leaves_parallel= True)
# história boa, dívida alta, garantias nenhuma, renda > 35
# história ruim, dívida alta, garantias adequada, renda < 15
# predict - faz a conta, estimativa de probabilidade
resultado = classificador.predict([[0,0,1,2], [3, 0, 0, 0]])
print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)