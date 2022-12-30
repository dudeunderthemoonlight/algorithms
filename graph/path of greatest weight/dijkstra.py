import math

with open('in3.txt', 'r') as infile:
    n = int(infile.readline())

    next_vertexes = [[]] * n  # списки смежности для каждой вершины, по индексу
    prevs = [[]] * n
    prev_vertexes = prevs.copy()

    for i in range(n):
        line = infile.readline()
        line_lst = line.split()
        lst = list(map(int, line_lst))

        zip_lst = list(zip(lst[::2], lst[1::2]))

        list_of_next = []
        for pair in zip_lst:
            v, s = pair
            npair = (v-1, s)
            prev_vertexes[npair[0]].append(i)

            list_of_next.append(npair)

        next_vertexes[i] = list_of_next

    start = int(infile.readline())
    finish = int(infile.readline())


d = [-math.inf] * n
d[start] = 0
used = [False] * n
previous = [-1] * n


def dijkstra():
    u = start
    while True:
        if u == n:
            break

        for i in range(n):
            if d[i] > d[u] and not used[i]:
                u = i

        used[u] = True
        for v, w in next_vertexes[u]:
            if d[v] < d[u] + w:
                d[v] = d[u] + w
                previous[v] = u

        u = u + 1


def write_result():
    with open("output.txt", 'w') as outfile:
        if d[finish - 1] == -math.inf:
            outfile.write("N")
        else:
            outfile.write("Y\n")

            current = finish
            result_lst = [current]
            while current != start:
                result_lst.append(previous[current])
                current = previous[current]

            result_lst.reverse()
            for vertex in result_lst:
                outfile.write(f'{vertex} ')
