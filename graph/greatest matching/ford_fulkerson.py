def has_cycle(path):  # проверка на цикл
    if len(path) > 2:
        without_last = path[:-1]
        elem = path[-1]
        return elem in without_last
    return False


# инпут - матрица смежности
def parse_input(file):
    with open(file, "r") as f:
        k, l = f.readline().split()
        k = int(k)
        l = int(l)
        matrix = [[] * l] * k
        for i in range(k):
            line = f.readline().split()
            matrix[i] = [int(x) for x in line]
    return k, l, matrix


#  f - поток, в самой программе (т.к. граф двудольный) используются два массива py[], px[] - это аналог f
class Graph:
    def __init__(self, in_file):
        self.k, self.l, self.matrix = parse_input(in_file)

        self.px = [-1] * self.k  # px[x] == y ~ f(x; y) == 1 (пустили поток по ребру (x; y))
        self.py = [-1] * self.l  # py[y] == x ~ f(x; y) == 1

        self.yt = [True] * self.l  # yt[y] == True ~ c(y; t) > 0 (True)

    # строим максимальный поток, если px[x] = y -> (x; y) в паросочетании
    # пробегаем все x, поиском в глубину ищем s-t цепь, останавливаемся если путей больше нет
    def ford_fulkerson(self):
        for x in range(self.k):
            if self.px[x] == -1:
                path = []
                self.dfs(x, path)

    # поиск идет всегда из X в Y, ПЕРЕХОДИМ в Y если:
    # 1) через вершину Y еще не проложен маршрут (т.е. поток == 0)
    # 2) еще не были в Y на этой итерации (храним путь - path, для избежания цикла)
    # 3) если есть путь (цепь) до T из X1, где py[Y] = X1
    #    (тут f(x; y) == 1 -> можем сразу перейти по Y в X1 -> f(x; y) станет == 0)
    def dfs(self, x, path):
        for y in range(self.l):

            if self.matrix[x][y] == 1:

                if self.py[y] == -1:  # (1)
                    if self.yt[y] is True:
                        self.yt[y] = False

                        self.py[y] = x
                        self.px[x] = y
                        return True

                else:
                    if self.py[y] == x:
                        continue

                    else:
                        path.append(y + self.k)  # добавляем Y в path перед переходом для проверки на цикл
                        if has_cycle(path):
                            path.pop()
                            continue  # если уже были в Y (цикл) то пропускаем его

                        if self.dfs(self.py[y], path):  # (3)

                            self.px[x] = y
                            self.py[y] = x
                            return True

                        continue

    def write_result(self, file_out):
        with open(file_out, 'w') as f:
            for x in range(self.k):
                f.write(f"{self.px[x] + 1} ")  # px[x] == y ~ (x; y) in M (паросочетание)


def main():
    graph = Graph("In4.txt")
    graph.ford_fulkerson()
    graph.write_result("output.txt")


if __name__ == '__main__':
    main()
