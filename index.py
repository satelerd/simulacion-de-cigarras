import numpy as np
import time
from function_grid import randMatrix, countFitness, gridCellFitness, animation
from alternative_fitness import gameOfLife

# Parameters
# -------------------
C1 = 4  # Fitness Prey
C2 = 7  # Fitness Predator
Numbers = [C1, C2]

lenMatrix = 200  # min 2
lenGenerations = 200

maxIndex = lenMatrix - 1
zeroMatrix = np.zeros((lenMatrix, lenMatrix))
matrixHistory = []  # list of all matrix generations
time1 = time.time()


# Start of the simulation
# -------------------
matrix = randMatrix(zeroMatrix, lenMatrix, Numbers)
matrixHistory.append(matrix)
print("Initial Matrix Created")
# print(matrix)
print()

print(f"Starting the simulation")
print()
# Main loop for each generation
for generation in range(0, lenGenerations):
    auxMatrix = matrixHistory[generation].copy()

    for i in range(0, lenMatrix):  # Matrix loop
        for j in range(0, lenMatrix):
            # print(matrixHistory[generation][i, j])

            # Get the neighbors of the current cell
            neighbors = countFitness(matrixHistory[generation], maxIndex, i, j)

            # Get the fitness of the current cell
            # auxMatrix[i, j] = gridCellFitness(neighbors, Numbers)
    
            # Game of Life mode
            auxMatrix[i, j] = gameOfLife(
                matrixHistory[generation][i, j], neighbors, Numbers
            )

    matrixHistory.append(auxMatrix)
time2 = time.time()
print(f"Simulation finished in {int(time2 - time1)} seconds")
print()
# -------------------
# End of the simulation


# Animation
# -------------------
print("Generating the animation")
print()
animation(matrixHistory, lenGenerations, lenMatrix, C1, C2)
