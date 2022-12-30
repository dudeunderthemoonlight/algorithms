infile = open('In.txt')

n = int(infile.readline())

adj_list = []
for i in range(n):
    s = infile.readline().split()
    lst = []
    for j in range(len(s)):
        if s[j] == '1':
            lst.append(j)
    adj_list.append(lst)


lst = []
visited = [False] * n


def result():
    res_lst = []
    lst.reverse()
    start = lst[0]
    for i in range(1, len(lst)):
        elem = lst[i]
        if elem == start:
            res_lst.append(start)
            res_lst.reverse()
            return res_lst
        else:
            res_lst.append(elem)


def cycle_found():
    with open('output.txt', 'w') as outfile:
        outfile.write("N\n")
        outfile.write(str(result()))
        infile.close()


def cycle_not_found():
    with open('output.txt', 'w') as outfile:
        outfile.write("A")
        infile.close()


def dfs(v, previous):
    visited[v] = True
    for i in adj_list[v]:
        if not visited[i]:
            lst.append(v + 1)
            dfs(i, v)
        else:
            if i != previous:
                lst.append(v + 1)
                lst.append(previous)
                cycle_found()
                exit(0)


for i in range(n):
    if not visited[i]:
        dfs(i, -1)
        cycle_not_found()
