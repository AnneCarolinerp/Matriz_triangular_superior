# -*- coding: utf-8 -*-
"""Matriz triangular superior"""

#Transformando M2 em uma matriz triangular superior, atribuindo zero a todos os elementos acima da diagonal principal
#M2
import numpy as np
def triangular_superior(m2):
  for linha in range(3):
    for coluna in range(3):
      if(linha > coluna):
        m2[linha][coluna] = 0
  return m2

m1 = np.array([[1, 2, 3], [5, 6, 7], [8, 9, 0]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(m1)
print("\n", triangular_superior(m2))