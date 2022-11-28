# the following is the logic for the game of life
def gameOfLife(itself, neighbor, Numbers):  # 0 = dead, 1 = live
    deadCount = neighbor.count(Numbers[0])
    liveCount = neighbor.count(Numbers[1])

    if itself == Numbers[1]:
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        if liveCount < 2:
            return Numbers[0]

        # Any live cell with two or three live neighbours lives on to the next generation.
        elif liveCount == 2 or liveCount == 3:
            return Numbers[1]

        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        elif liveCount > 3:
            return Numbers[0]

    elif itself == Numbers[0]:
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        if liveCount == 3:
            return Numbers[1]
        else:
            return itself

    else:
        print("Error")

    # if M[i, j] == Numbers[0]:
    #     deadCount += 1
    # else:
    #     liveCount += 1

    # # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # if liveCount < 2:
    #     return Numbers[0]

    # # Any live cell with two or three live neighbours lives on to the next generation.
    # elif liveCount == 2 or liveCount == 3:
    #     return Numbers[1]

    # # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # elif liveCount > 3:
    #     return Numbers[0]

    # # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    # elif deadCount == 3:
    #     return Numbers[1]

    # else:
    #     return M[i, j]
