# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:44:56 2019

@author: wesleysa
"""

Census
-------------------------------------

0.4767 - Naive Bayes (labelenconder + onehotenconder + escalonamento)
0.7952 - Naive Bayes (labelenconder)
0.7950 - Naive Bayes (labelenconder _ onehotencoder)
0.8057 - Naive Bayes (labelencoder + escalonamento)

0.8102 - Árvore de decisão (labelencoder + onehotencoder + escalonamento)
0.8128 - Árvore de decisão (labelencoder)
0.8102 - Árvore de decisão (labelencoder + oneotencoder)
0.8128 - Árvore de decisão (labelencoder + escalonamento)

0.8476 - Random forest n_estimators = 40 (labelenconder + onehotencoder + escalonamento)
0.8481 - Random forest n_estimators = 40 (labelencoder)
0.8489 - Random forest (labelencoder + onehotencoder)
0.8479 - Random forest (labelencoder + escalonamento)