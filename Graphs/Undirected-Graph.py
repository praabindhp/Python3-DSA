# Graphs
# Implement a simple undirected graph class using adjacency list representation. The class should have the following methods:

# add_node(node) - Adds a node to the graph.

# add_edge(node1, node2) - Adds an undirected edge between node1 and node2.

# has_edge(node1, node2) - Returns True if there is an undirected edge between node1 and node2, and False otherwise.

# Example:

# graph = UndirectedGraph()
# graph.add_node(1)
# graph.add_node(2)
# graph.add_node(3)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
 
# print(graph.has_edge(1, 2))  # Should print True
# print(graph.has_edge(1, 3))  # Should print False

# Python code
class UndirectedGraph:
  def __init__(self):
    self.adjacency_list = {}

  def add_node(self, node):
    self.adjacency_list[node] = []

  def add_edge(self, node1, node2):
    self.adjacency_list[node1].append(node2)
    self.adjacency_list[node2].append(node1)

  def has_edge(self, node1, node2):
    return node2 in self.adjacency_list[node1]
