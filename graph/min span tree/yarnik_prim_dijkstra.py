import math


class Graph:
    def __init__(self, in_file):
        self.n, self.matrix = self.parse_input(in_file)  # n - vertex's amount, matrix - matrix of weights
        self.min_span, self.weight_span = self.find_min_span()

    def find_min_span(self):  # yarnik-prim-dijkstra algorithm
        min_span = set()
        weight = 0  # weight of minimal span
        d = [math.inf] * self.n  # distance from i-vertex to span
        p = [math.inf] * self.n  # lightest previous vertex to i-vertex

        # priority queue, list realization
        q = [i for i in range(self.n)]

        d[0] = 0

        # get the "lightest" vertex according to d[]
        v = self.extract_min(q, d)

        while q:
            adjacent = self.matrix[v]
            for i in range(self.n):
                if adjacent[i] != 32767:
                    u = i  # one of adjacent vertexes to v

                    #  if u not in span, and weight (v, u) < distance to span
                    if u in q and (self.matrix[v][u] < d[u]):
                        d[u] = self.matrix[v][u]
                        p[u] = v

            v = self.extract_min(q, d)

            min_span.add((p[v], v))
            weight += self.matrix[v][p[v]]

        return min_span, weight

    # return the "lightest" vertex and delete it from queue q
    @staticmethod
    def extract_min(q, d):
        min_vertex = q[0]
        for vertex in q:
            if d[vertex] < d[min_vertex]:
                min_vertex = vertex
        q.remove(min_vertex)
        return min_vertex

    @staticmethod
    def parse_input(file):
        with open(file, "r") as f:
            n = int(f.readline())

            matrix = [[] * n] * n
            for i in range(n):
                line = f.readline().split()
                matrix[i] = [int(x) for x in line]

        return n, matrix

    def write_min_span_as_adj_list(self, file):
        with open(file, 'w') as f:
            for i in range(self.n):
                adj_list = []
                for prev, vertex in self.min_span:
                    if prev == i:
                        adj_list.append(vertex)
                    if vertex == i:
                        adj_list.append(prev)

                adj_list.sort()
                adj_list.append(-1)

                for elem in adj_list:
                    f.write(f"{str(elem + 1)} ")
                f.write("\n")

            f.write(str(self.weight_span))


def main():
    graph = Graph("input.txt")
    graph.write_min_span_as_adj_list("output.txt")


if __name__ == '__main__':
    main()
