import numpy as np
from function_grid import countFitness, gridCellFitness

# Parameters
# -------------------
C1 = 4  # Fitness Prey
C2 = 7  # Fitness Predator
Numbers = [C1, C2]

lenMatrix = 10  # min 2
maxIndex = lenMatrix - 1
zeroMatrix = np.zeros((lenMatrix, lenMatrix))


# Random matrix
# -------------------
print("----------------------------------------")


def randMatrix(matrix):
    cont = 0
    for i in range(0, lenMatrix):
        for j in range(0, lenMatrix):
            matrix[i, j] = np.random.choice(Numbers)
    return matrix


matrix = randMatrix(zeroMatrix)
print(matrix)


# Fitness for each value of the matrix
# -------------------
auxMatrix = matrix.copy()
for i in range(0, lenMatrix):
    for j in range(0, lenMatrix):
        neighbors = countFitness(matrix, maxIndex, i, j)
        # neighbors=np.array(neighbors)
        auxMatrix[i, j] = gridCellFitness(neighbors)
        print(gridCellFitness(neighbors))
print(matrix)
print("---------------------------")
print(auxMatrix)


# print(countFitness(matrix, maxIndex, 5, 6))
