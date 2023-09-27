from collections import defaultdict, deque


class DAG:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edges(self, start, end):
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)

    def print_dag(self):
        for vertex, neighbors in self.graph.items():
            print(vertex, neighbors)

    def topological_sort(self):
        in_degree_map = defaultdict(int)
        topological_order = []
        for vertex, in self.graph:
            for neighbor in self.graph[vertex]:
                if vertex not in in_degree_map:
                    in_degree_map[vertex] = 0
                in_degree_map[neighbor] += 1
        queue = deque([vertex for vertex in self.graph if in_degree_map[vertex] == 0])
        while queue:
            current_vertex = queue.popleft()
            topological_order.append(current_vertex)
            for neighbor in self.graph[current_vertex]:
                in_degree_map[neighbor] -= 1
                if in_degree_map[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_order) == len(self.graph):
            return topological_order
        else:
            return []

        print(in_degree_map)


dag = DAG()

dag.add_vertex("A")
dag.add_vertex("B")
dag.add_vertex("C")
dag.add_vertex("D")

dag.add_edges("A", "B")
dag.add_edges("B", "C")
dag.add_edges("A", "C")
dag.add_edges("C", "D")

print(dag.topological_sort())
