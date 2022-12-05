import numpy as np


def randMatrix(matrix, lenMatrix, numbers):
    cont = 0
    for i in range(0, lenMatrix):
        for j in range(0, lenMatrix):
            matrix[i, j] = np.random.choice(numbers)
    return matrix


def arrayFunction(X, Y, T):  # X e Y son los valores de las posiciones en la matriz X la posición central e Y con la que la comparamos
    xList = []
    yList = []
    for i in range(1, T+1):
        if (i % X == 0):
            xList.append(1)
        else:
            xList.append(0)
        if (i % Y == 0):
            yList.append(1)
        else:
            yList.append(0)
    if ((X == Y)):
        return np.array([xList])

    else:
        return np.array([xList, yList])






def f1(array):  # f1 predator

    shape = np.shape(array)
    fit = 0
    if (shape[0] == 1):
        for i in range(0, shape[1]):
            if (array[0, i] == 1):
                fit -= 1
    else:
        for i in range(0, shape[1]):
            if (array[0, i] == 1 and array[1, i] == 0):
                fit -= 1
            if (array[0, i] == 1 and array[1, i] == 1):
                fit += 1
    return fit


def f2(array):  # f2 Prey

    shape = np.shape(array)
    fit = 0
    if (shape[0] == 1):
        for i in range(0, shape[1]):
            if (array[0, i] == 1):
                fit += 1
    else:
        for i in range(0, shape[1]):
            if (array[0, i] == 1 and array[1, i] == 0):
                fit += 1
            if (array[0, i] == 1 and array[1, i] == 1):
                fit -= 1
    return fit


# Get the fitness of the current cell ()


def F(M,neighbor, Numbers, value, T):
    if (value == Numbers[0]):  # predator
        fit=0
        for i in range(0,np.shape(neighbor)[0]):
            fit+=f1(arrayFunction(value,M[neighbor[i,0],neighbor[i,1]],T))
        return ((1/Numbers[1])*fit)    
    else:
        fit=0
        for i in range(0,np.shape(neighbor)[0]):
            fit+=f2(arrayFunction(value,M[neighbor[i,0],neighbor[i,1]],T))
        return ((1/Numbers[0])*fit)   


def cellElection(N1,N2,N3,N4,value,List,M):
    position=0
    
    for i in range(0,len(List)):
        if (List[i]>=position):
            position=i
    if (position==0):
        return M[N1[0],N1[1]]
    elif(position==1):
        return M[N2[0],N2[1]]
            
    elif(position==2):
        return M[N3[0],N3[1]]
            
    elif(position==3):
        return M[N4[0],N4[1]]
        
    elif(position==4):
        return M[value[0],value[1]]
        
    #for i in np.shape(neighbor)[0]


def animation(matrixHistory, lenGenerations, lenMatrix, A, B):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    # 7 es amarillo y 4 morado (creo, no se como se decidio eso, pero funciona)
    fig = plt.figure()
    ims = []
    for i in range(0, lenGenerations):
        im = plt.imshow(matrixHistory[i], animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(
        fig, ims, interval=50, blit=True, repeat_delay=500
    )  # interval es el tiempo entre cada generación
    plt.title("Investigación De Cigarras")
    plt.xlabel(f"{A} = Predator, {B}= Prey")
    plt.colorbar()
    plt.show()


# M: matrix to take neighbors, large: matrix size, X: row number of the current cell, Y: column number of the current cel
# en alternativa, debe retornar las posiciones de los vecinos
def countNeighbors(M, large, X, Y):
    if Y == 0:
        if X == 0:
            neighbors = [
                [X + 1, Y],
                [X, Y + 1],
                [large, Y],
                [X, large],
            ]
        elif X == large:
            neighbors = [
                [X - 1, Y],
                [X, Y + 1],
                [0, 0],
                [X, large],
            ]
        else:
            neighbors = [
                [X + 1, Y],
                [X - 1, Y],
                [X, Y + 1],
                [X, large],
            ]

    elif X == 0 and Y != 0:
        if Y == large:
            neighbors = [
                [X, Y - 1],
                [X + 1, Y],
                [X, 0],
                [large, Y],
            ]
        else:
            neighbors = [
                [X, Y - 1],
                [X, Y + 1],
                [X + 1, Y],
                [large, Y],
            ]

    elif X == large and Y != 0:
        if Y == large:
            neighbors = [
                [X, Y - 1],
                [X - 1, Y],
                [0, Y],
                [X, 0],
            ]
        else:
            neighbors = [
                [X, Y - 1],
                [X, Y + 1],
                [X - 1, Y],
                [0, Y],
            ]

    elif Y == large and ((X != large) or (X != 0)):
        neighbors = [
            [X, Y - 1],
            [X + 1, Y],
            [X - 1, Y],
            [X, 0],

        ]

    else:
        neighbors = [
            [X + 1, Y],
            [X - 1, Y],
            [X, Y + 1],
            [X, Y - 1],

        ]

    return np.array(neighbors)
