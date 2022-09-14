import numpy as np
from function_grid import countFitness
# Inicialización del modelo

C1 = 4  # Fitness Prey

C2 = 8  # Fitness Predator
Numbers = [C1, C2]
LenMatrix = 10
MaxIndex= LenMatrix-1
matrix = np.zeros((LenMatrix, LenMatrix))

print("----------------------------------------")
cont=0
for i in range(0, LenMatrix):
    for j in range(0, LenMatrix):

        matrix[i, j] = np.random.choice(Numbers)


print(matrix)
#--------------------------------------------------------------------------------
# Inicio de las iteraciones

T_Max = 100  # max iteraciones (de momento)

print(countFitness(matrix, MaxIndex, 5, 6))




