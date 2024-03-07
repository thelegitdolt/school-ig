class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = dict()

    def add_neighbor(self, node, weight=0):
        self.connected_to[node] = weight

class Graph:
    def __init__(self):
        self.vert_list = dict()
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_ver = Vertex(key)
        self.vert_list[key] = new_ver
        return new_ver

    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            new_ver = self.add_vertex(f)
        if t not in self.vert_list:
            new_ver = self.add_vertex(f)

        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def __iter__(self):
        return self.vert_list.values().__iter__()
