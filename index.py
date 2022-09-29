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
lenGenerations = 10
matrixHistory = []


# Start of the simulation
# -------------------
matrix = randMatrix(zeroMatrix, lenMatrix, Numbers)
print("Initial Matrix")
print(matrix)
print()

# Main loop for each generation
for generation in range(0, lenGenerations):
    if generation == 0:
        auxMatrix = matrix.copy()

    else:
        auxMatrix = matrixHistory[generation - 1].copy()

    for i in range(0, lenMatrix):  # Matrix loop
        for j in range(0, lenMatrix):
            neighbors = countFitness(matrix, maxIndex, i, j)  # Fitness for the cell
            auxMatrix[i, j] = gridCellFitness(neighbors)

    matrixHistory.append(auxMatrix)

print("Fitness Matrix")
print(auxMatrix)
# print(matrix)
print()

print("Matrix History")
for i in range(0, lenGenerations):
    print(matrixHistory[i])
    print()
