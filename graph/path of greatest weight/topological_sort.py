import math
import copy

def my_copy(a):
    new_lst = []
    for el in a:
        new_list = list(el)
        new_lst.append(new_list)
    return new_lst


with open('In3.txt', 'r') as infile:
    n = int(infile.readline())

    next_vertexes = [[]] * n  # списки смежности для каждой вершины, по индексу
    prevs = [[]] * n
    prev_vertexes = my_copy(prevs)

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

    start = int(infile.readline()) - 1
    finish = int(infile.readline()) - 1


def remove_vertex(next_lsts, elem):
    new_next_lsts = copy.deepcopy(next_lsts)
    for j in range(len(new_next_lsts)):
        if j == elem:
            new_next_lsts[j] = [[-math.inf, -math.inf]]

        new_next_lsts[j] = [(x, y) for (x, y) in new_next_lsts[j] if x != elem]
    return new_next_lsts


def topological_sort():
    new_next = copy.deepcopy(next_vertexes)
    changed_vertex = [[]] * n
    max_unused = n-1
    used = [False] * n

    for i in range(n):
        if next_vertexes[i] == [] and prev_vertexes[i] == []:
            changed_vertex[i] = max_unused
            max_unused -= 1
            used[i] = True

    while max_unused != -1:
        for i in range(len(next_vertexes)):
            if not new_next[i] and not used[i]:
                changed_vertex[i] = max_unused
                new_next = remove_vertex(new_next, i)
                max_unused -= 1
                used[i] = True
    return changed_vertex


d = [-math.inf] * n
used = [False] * n
previous = [-1] * n
changed_vertex = topological_sort()


def write_result(start, finish):
    with open("output.txt", 'w') as outfile:
        if d[finish] == -math.inf:
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
                outfile.write(f'{changed_vertex[vertex] + 1} ')
            outfile.write(f'\n{d[finish]}')


def rename_graph(changed_vertex):
    new_next = [[]] * n
    for i in range(len(next_vertexes)):
        new_i = changed_vertex[i]
        i_list = next_vertexes[i]
        new_i_list = []
        for v, s in i_list:
            nv = changed_vertex[v]
            new_pair = (nv, s)
            new_i_list.append(new_pair)
        new_next[new_i] = new_i_list
    return new_next


def find_dist(next_vertexes, changed_vertex):
    new_start = changed_vertex[start]
    new_finish = changed_vertex[finish]
    d[new_start] = 0

    u = new_start

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

    return new_start, new_finish


if __name__ == '__main__':
    new_next_vertexes = rename_graph(changed_vertex)
    start, finish = find_dist(new_next_vertexes, changed_vertex)
    write_result(start, finish)


