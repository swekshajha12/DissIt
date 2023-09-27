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


dag = DAG()

dag.add_vertex("A")
dag.add_vertex("B")
dag.add_vertex("C")
dag.add_vertex("D")

dag.add_edges("A", "B")
dag.add_edges("B", "C")
dag.add_edges("A", "C")
dag.add_edges("C", "D")

dag.print_dag()
