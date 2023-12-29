class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}
        
    def addNode(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            
    def addEdge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
        
    def removeEdge(self, node1, node2):
        if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
            self.adjacency_list[node1].remove(node2)
            self.adjacency_list[node2].remove(node1)
            
    def removeNode(self, node):
        if node in self.adjacency_list:
            for neighbor in self.adjacency_list[node]:
                self.adjacency_list[neighbor].remove(node)
            del self.adjacency_list[node]
            
    def display(self):
        for node in self.adjacency_list:
            print(node, ":", self.adjacency_list[node])