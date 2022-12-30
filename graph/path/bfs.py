from collections import deque

with open('In.txt', 'r') as inline:
    n = int(inline.readline())
    m = int(inline.readline())

    labyrinth = []
    for i in range(n):
        rawRow = inline.readline().split()
        row = [int(item) for item in rawRow]
        labyrinth.append(row)

    rowStart = inline.readline().split()
    start = [int(item) for item in rowStart]

    rowFinish = inline.readline().split()
    finish = [int(item) for item in rowFinish]

q = deque()
q.append(start)

dirX = [0, 0, -1, 1]
dirY = [-1, 1, 0, 0]

dist = [[0] * m for _ in range(n)]

dist[start[0] - 1][start[1] - 1] = 1

while q:
    point = q.popleft()
    oldY = point[0]
    oldX = point[1]

    for i in range(4):

        y = oldY + dirY[i]
        x = oldX + dirX[i]
        newPoint = [y, x]

        if (labyrinth[y - 1][x - 1] == 0) & (dist[y - 1][x - 1] == 0):
            dist[y - 1][x - 1] = dist[oldY - 1][oldX - 1] + 1
            q.append(newPoint)


def getresult():
    with open("output.txt", 'w') as outfile:
        if dist[finish[0] - 1][finish[1] - 1] == 0:
            outfile.write("N")
        else:
            outfile.write("Y\n")
            path = make_path()
            for item in path:
                y = item[0]
                x = item[1]
                outfile.write("{0} {1}\n".format(y, x))


def make_path():
    path = [finish]
    curr_point = finish
    while curr_point != start:
        old_x = curr_point[1]
        old_y = curr_point[0]
        for j in range(4):
            y = old_y + dirY[j]
            x = old_x + dirX[j]
            new_point = [y, x]
            if dist[y - 1][x - 1] == dist[old_y - 1][old_x - 1] - 1:
                path.append(new_point)
                curr_point = path[-1]
    path.reverse()
    return path


getresult()
