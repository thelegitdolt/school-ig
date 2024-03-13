class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
        
    def delNeighbor(self, nbr):
        if nbr in self.connectedTo:
            del self.connectedTo[nbr]
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def __repr__(self):
        return self.id.__str__()
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = dict()
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertList[key] = new_vertex
        return new_vertex
    
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        
    def get_by_id(self, value):
        for v in self.vertList.values():
            if value == v.id:
                return v
            
    
    def __contains__(self, key):
        if isinstance(key, Vertex):
            return key.id in self.vertList
        return key in self.vertList
    
    def addEdge(self, from_, to, weight=0):
        if from_ not in self.vertList:
            self.addVertex(from_)
        if to not in self.vertList:
            self.addVertex(to)
        
        self.vertList[from_].addNeighbor(self.vertList[to], weight)
    
    def removeEdge(self, from_, to):
        self.vertList[from_].delNeighbor(to)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, index):
        start, queue, traversal = self.vertList[index], [], []
        queue.append(start)
        
        while not len(queue) == 0:
            v = queue.pop(0)
            if v.id in traversal:
                continue
                
            traversal.append(v.id)
            for vertex in v.connectedTo.keys():
                queue.append(vertex)
        return traversal
    
    def depth_first_search(self):
        for v in self.vertList.values():
            v.color = 'white'
        path = []  # not a part of DFS, used to check the order of vertices traversed by DFS
        for v in self.vertList.values():
            if v.color == 'white':
                self.DFS(v.id, path)
        return path
    
    def DFS(self, vid, path):
        v = self.vertList[vid]
        v.color = 'gray'
        path.append(v.id)
        for u in v.connectedTo.keys():
            if u.color == 'white':
                self.DFS(u.id, path)
        v.color = 'black'
        return path

    