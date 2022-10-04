import numpy as np
from function_grid import randMatrix, countFitness, gridCellFitness, animation

# Parameters
# -------------------
C1 = 4  # Fitness Prey
C2 = 7  # Fitness Predator
Numbers = [C1, C2]

lenMatrix = 100  # min 2
maxIndex = lenMatrix - 1
zeroMatrix = np.zeros((lenMatrix, lenMatrix))
lenGenerations = 200
matrixHistory = []  # list of all matrix generations


# Start of the simulation
# -------------------
matrix = randMatrix(zeroMatrix, lenMatrix, Numbers)
matrixHistory.append(matrix)
print("Initial Matrix")
print(matrix)
print()

# Main loop for each generation
for generation in range(0, lenGenerations):
    auxMatrix = matrixHistory[generation].copy()

    for i in range(0, lenMatrix):  # Matrix loop
        for j in range(0, lenMatrix):
            neighbors = countFitness(
                matrixHistory[generation], maxIndex, i, j
            )  # Fitness for the cell
            auxMatrix[i, j] = gridCellFitness(neighbors,Numbers)

    matrixHistory.append(auxMatrix)

# -------------------
# End of the simulation


# Prints
# -------------------
print("Fitness Matrix")
print(auxMatrix)
# print(matrix)
print()

# print("Matrix History")
# for i in range(0, lenGenerations):
#     print(matrixHistory[i])
#     print()

# Animation
# -------------------
animation(matrixHistory, lenGenerations, lenMatrix,C1,C2)
