import numpy as np
import time
from function_grid import randMatrix, countNeighbors,F, animation, cellElection
from alternative_fitness import gameOfLife
# Parameters
# -------------------
C1 = 4  # Fitness Predator
C2 = 2  # Fitness Prey
T=C1*C2
Numbers = [C1, C2]

lenMatrix = 15  # min 2
lenGenerations = 3*2*lenMatrix*3

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
    x_param= np.random.randint(lenMatrix)
    y_param= np.random.randint(lenMatrix)
    fitnessCompare=[]
    # Get the neighbors of the current cell
    # Get the fitness of the current cell
    value=auxMatrix[x_param, y_param]
    neighbors = countNeighbors(matrixHistory[generation], maxIndex, x_param, y_param)
    #----------------------------------------------------------------------------------
    
    N1=neighbors[0]
    neighbors1 = countNeighbors(matrixHistory[generation], maxIndex, N1[0], N1[1])
    fitnessCompare.append(F(auxMatrix,neighbors1,Numbers, auxMatrix[N1[0],N1[1]],T))
    #----------------------------------------------------------------------------------
    
    N2=neighbors[1]
    neighbors2 = countNeighbors(matrixHistory[generation], maxIndex, N2[0], N2[1])
    fitnessCompare.append(F(auxMatrix,neighbors2,Numbers, auxMatrix[N2[0],N2[1]],T))
    
    #----------------------------------------------------------------------------------
    
    N3=neighbors[2]
    neighbors3 = countNeighbors(matrixHistory[generation], maxIndex, N3[0], N3[1])
    fitnessCompare.append(F(auxMatrix,neighbors3,Numbers, auxMatrix[N3[0],N3[1]],T))
    
    #----------------------------------------------------------------------------------
    
    N4=neighbors[3]
    neighbors4 = countNeighbors(matrixHistory[generation], maxIndex, N4[0], N4[1])
    fitnessCompare.append(F(auxMatrix,neighbors4,Numbers, auxMatrix[N4[0],N4[1]],T))
    
    #----------------------------------------------------------------------------------
    
    fitnessCompare.append(F(auxMatrix,neighbors,Numbers, value,T))
    for i in range(0,len(fitnessCompare)):
        fitnessCompare[i]=np.round(fitnessCompare[i],2)    
    print(fitnessCompare)
    matrixHistory.append(auxMatrix)
    
    if (value==auxMatrix[N1[0],N1[1]] and value==auxMatrix[N2[0],N2[1]] and value==auxMatrix[N3[0],N3[1]] and value==auxMatrix[N4[0],N4[1]] and value==Numbers[0]):
        auxMatrix[x_param,y_param]=np.nan
    elif(value!=Numbers[0] and value!=Numbers[1]):
        continue
    else:
        auxMatrix[x_param,y_param]= cellElection(N1,N2,N3,N4,[x_param,y_param],fitnessCompare,auxMatrix)
    
    
    
    #----------------------------------------------------------------------------------
    
    
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
