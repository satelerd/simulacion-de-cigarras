import numpy as np


# M: matrix to take neighbors, large: matrix size, X: row number of the current cell, Y: column number of the current cell
def countFitness(M, large, X, Y):

    if(Y == 0):
        if(X == 0):
            neighbors = [M[X+1, Y], M[X+1, Y+1], M[X, Y+1], M[large, Y],
                         M[large, Y+1], M[X, large], M[X+1, large], M[large, large]]
        elif(X == large):
            neighbors = [M[X-1, Y], M[X-1, Y+1], M[X, Y+1], M[X,
                                                              large], M[X-1, large], M[0, 0], M[0, 1], M[0, large]]
        else:
            neighbors = [M[X+1, Y], M[X-1, Y], M[X+1, Y+1], M[X, Y+1],
                         M[X-1, Y+1], M[X+1, large], M[X, large], M[X-1, large]]
    elif(X == 0):
        if(Y == large):
            neighbors = [M[X, Y-1], M[X+1, Y], M[X+1, Y-1], M[X, 0],
                         M[X+1, 0], M[large, Y], M[large, Y-1], M[large, large]]
        else:
            neighbors = [M[X, Y-1], M[X, Y+1], M[X+1, Y], M[X+1, Y-1],
                         M[X+1, Y+1], M[large, Y-1], M[large, Y], M[large, Y+1]]
    elif(X == large):
        if(Y == large):
            neighbors = [M[X, Y-1], M[X-1, Y], M[X-1, Y-1],
                         M[0, Y], M[0, Y-1], M[X, 0], M[X-1, 0], M[0, 0]]
        else:
            neighbors = [M[X, Y-1], M[X, Y+1], M[X-1, Y], M[X-1,
                                                            Y-1], M[X-1, Y+1], M[0, Y], M[0, Y-1], M[0, Y+1]]
    elif(Y == large and ((X != large) or (X != 0))):
        neighbors = [M[X, Y-1], M[X-1, Y-1], M[X+1, Y-1],
                     M[X+1, Y], M[X-1, Y], M[X, 0], M[X+1, 0], M[X-1, 0]]
    else:
        neighbors = [M[X+1, Y], M[X-1, Y], M[X, Y+1], M[X+1, Y+1],
                     M[X-1, Y+1], M[X+1, Y-1], M[X, Y-1], M[X-1, Y-1]]

    return neighbors


def gridCellFitness(neighbor):  #funcion que retorna el fitness asociado a cada celda, lo calculca por celda
    fitness= sum(neighbor)
    return fitness