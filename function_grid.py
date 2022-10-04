import numpy as np


def randMatrix(matrix, lenMatrix, numbers):
    cont = 0
    for i in range(0, lenMatrix):
        for j in range(0, lenMatrix):
            matrix[i, j] = np.random.choice(numbers)
    return matrix


# M: matrix to take neighbors, large: matrix size, X: row number of the current cell, Y: column number of the current cel
def countFitness(M, large, X, Y):
    if Y == 0:
        if X == 0:
            neighbors = [
                M[X + 1, Y],
                M[X + 1, Y + 1],
                M[X, Y + 1],
                M[large, Y],
                M[large, Y + 1],
                M[X, large],
                M[X + 1, large],
                M[large, large],
            ]
        elif X == large:
            neighbors = [
                M[X - 1, Y],
                M[X - 1, Y + 1],
                M[X, Y + 1],
                M[X, large],
                M[X - 1, large],
                M[0, 0],
                M[0, 1],
                M[0, large],
            ]
        else:
            neighbors = [
                M[X + 1, Y],
                M[X - 1, Y],
                M[X + 1, Y + 1],
                M[X, Y + 1],
                M[X - 1, Y + 1],
                M[X + 1, large],
                M[X, large],
                M[X - 1, large],
            ]

    elif X == 0:
        if Y == large:
            neighbors = [
                M[X, Y - 1],
                M[X + 1, Y],
                M[X + 1, Y - 1],
                M[X, 0],
                M[X + 1, 0],
                M[large, Y],
                M[large, Y - 1],
                M[large, large],
            ]
        else:
            neighbors = [
                M[X, Y - 1],
                M[X, Y + 1],
                M[X + 1, Y],
                M[X + 1, Y - 1],
                M[X + 1, Y + 1],
                M[large, Y - 1],
                M[large, Y],
                M[large, Y + 1],
            ]

    elif X == large:
        if Y == large:
            neighbors = [
                M[X, Y - 1],
                M[X - 1, Y],
                M[X - 1, Y - 1],
                M[0, Y],
                M[0, Y - 1],
                M[X, 0],
                M[X - 1, 0],
                M[0, 0],
            ]
        else:
            neighbors = [
                M[X, Y - 1],
                M[X, Y + 1],
                M[X - 1, Y],
                M[X - 1, Y - 1],
                M[X - 1, Y + 1],
                M[0, Y],
                M[0, Y - 1],
                M[0, Y + 1],
            ]

    elif Y == large and ((X != large) or (X != 0)):
        neighbors = [
            M[X, Y - 1],
            M[X - 1, Y - 1],
            M[X + 1, Y - 1],
            M[X + 1, Y],
            M[X - 1, Y],
            M[X, 0],
            M[X + 1, 0],
            M[X - 1, 0],
        ]

    else:
        neighbors = [
            M[X + 1, Y],
            M[X - 1, Y],
            M[X, Y + 1],
            M[X + 1, Y + 1],
            M[X - 1, Y + 1],
            M[X + 1, Y - 1],
            M[X, Y - 1],
            M[X - 1, Y - 1],
        ]

    return neighbors


# Get the fitness of the current cell (the value that repeats the most)
def gridCellFitness(neighbor,Numbers):
    Valor1=neighbor.count(Numbers[0])
    Valor2=neighbor.count(Numbers[1])
    if( Valor1<Valor2):
        return Numbers[1]
    elif(Valor1>Valor2):
        return Numbers[0]
    else:
        return np.random.choice(Numbers)
    #print(neighbor)
    #print(fitness)
    #return fitness


def animation(matrixHistory, lenGenerations, lenMatrix,A,B):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    # 7 es amarillo y 4 morado (creo, no se como se decidio eso, pero funciona)
    fig = plt.figure()
    ims = []
    for i in range(0, lenGenerations):
        im = plt.imshow(matrixHistory[i], animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(
        fig, ims, interval=200, blit=True, repeat_delay=500
    )  # interval es el tiempo entre cada generación
    plt.title("Investigación De Cigarras")
    plt.xlabel(f"{A} = Prey, {B}= Predator")
    plt.colorbar()
    plt.show()
