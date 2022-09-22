import numpy as np
from function_grid import randMatrix, countFitness, gridCellFitness

# Parameters
# -------------------
C1 = 4  # Fitness Prey
C2 = 7  # Fitness Predator
Numbers = [C1, C2]

lenMatrix = 10  # min 2
maxIndex = lenMatrix - 1
zeroMatrix = np.zeros((lenMatrix, lenMatrix))


# Start of the simulation
# -------------------
matrix = randMatrix(zeroMatrix)
print("Initial Matrix")
print(matrix)
print()


# Fitness for each value of the matrix
auxMatrix = matrix.copy()
for i in range(0, lenMatrix):  # Matrix loop
    for j in range(0, lenMatrix):
        neighbors = countFitness(matrix, maxIndex, i, j)
        # neighbors=np.array(neighbors)
        auxMatrix[i, j] = gridCellFitness(neighbors)
        print(gridCellFitness(neighbors))

print("Fitness Matrix")
print(auxMatrix)
# print(matrix)
print()
