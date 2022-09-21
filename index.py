import numpy as np
from function_grid import countFitness, gridCellFitness

# Inicialización del modelo
# -------------------


# Parametros
# -------------------
C1 = 4  # Fitness Prey
C2 = 7  # Fitness Predator
Numbers = [C1, C2]

LenMatrix = 10  # mínimo 2
MaxIndex = LenMatrix - 1
matrix = np.zeros((LenMatrix, LenMatrix))


# Matriz aleatoria
# -------------------
print("----------------------------------------")
cont = 0
for i in range(0, LenMatrix):
    for j in range(0, LenMatrix):
        matrix[i, j] = np.random.choice(Numbers)

print(matrix)


# Fitness por cada dato de la matriz
# -------------------
T_Max = 100  # max iteraciones (de momento)
matrix_Aux = matrix.copy()
for i in range(0, LenMatrix):
    for j in range(0, LenMatrix):
        neighbors = countFitness(matrix, MaxIndex, i, j)
        #    neighbors=np.array(neighbors)
        matrix_Aux[i, j] = gridCellFitness(neighbors)
        print(gridCellFitness(neighbors))
print(matrix)
print("---------------------------")
print(matrix_Aux)


# print(countFitness(matrix, MaxIndex, 5, 6))
