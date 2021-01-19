'''

We are given a simple undirected graph G = (V,E) and a 
set of vertices T in subset V. We want to compute the
set of vertices that is reachable from a specific starting
vertex s using a path that visits at most k vertices of T.

Design an algorithm that computes all vertices G that are reachable
from s using a path that contains at most k vertices of T. For full marks your algorithm needs
to run in O(n+m) time.

'''


class Graph():
    #creating simple undirected graph structure
    def __init__(self):
        self.vertices_no = 0
        self.adjacencylist = {}
        self.T_list = []

    def add_vertex(self, v):
      if v in self.adjacencylist:
        print("Vertex ", v, " already exists.")
      else:
        self.vertices_no = self.vertices_no + 1
        self.adjacencylist[v] = []
        if 'T' in v:
            self.T_list.append(v)

    # Add an edge between vertex v1 and v2 w
    def add_edge(self, v1, v2):
      # Check if vertex v1 is a valid vertex
      if v1 not in self.adjacencylist:
        print("Vertex ", v1, " does not exist.")
      # Check if vertex v2 is a valid vertex
      elif v2 not in self.adjacencylist:
        print("Vertex ", v2, " does not exist.")
      else:
        #undirected implementation
        self.adjacencylist[v1].append(v2)
        self.adjacencylist[v2].append(v1)

    # Print the graph
    def print_graph(self):
      for vertex in self.adjacencylist:
          print(vertex, " -> ", self.adjacencylist[vertex])

    # Implementing modified BFS
    def BFS(self, s, k):
      adjacencyList = self.adjacencylist
      visited = [s]

      #original layer counters
      layers = []
      curr_layer = []
      next_layer = []

      #T layer counters
      T_curr_layer = []
      T_next_layer = []
      layer_T = 0

      if s not in self.T_list:
          curr_layer.append(s)
      else:
          T_curr_layer.append(s)

      while len(curr_layer) > 0 or len(T_curr_layer) > 0:
          if len(curr_layer) > 0:
              layers.extend(curr_layer)
              for u in curr_layer:
                for v in adjacencyList[u]:
                  if v not in visited:
                    if v not in self.T_list:
                      next_layer.append(v)
                    else:
                      T_curr_layer.append(v)
                    visited.append(v)
              curr_layer = next_layer
              next_layer = []
          else:
              layer_T +=1
              if layer_T > k: break
              layers.extend(T_curr_layer)
              for u in T_curr_layer:
                for v in adjacencyList[u]:
                  if v not in visited:
                    if v not in self.T_list:
                      curr_layer.append(v)
                    else:
                      T_next_layer.append(v)
                    visited.append(v)
              T_curr_layer = T_next_layer
              T_next_layer = []

      return layers



    # def DFS_helper(self, vertex):
    #   if not vertex: return None
    #   visited[vertex] = True
    #   result.append(vertex)
    #   for neighbour in self.adjacencylist[vertex]:
    #     if neighbour not in visited.keys():
    #       return DFS_helper(neighbour)





# driver code
g = Graph()
# stores the number of vertices in the graph
g.add_vertex('A')
g.add_vertex('TX')
g.add_vertex('T1')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_vertex('T3')
g.add_vertex('T2')
g.add_vertex('J')
g.add_vertex('T4')
g.add_vertex('T5')
g.add_vertex('M')
g.add_vertex('N')
g.add_vertex('O')
g.add_vertex('P')
g.add_vertex('T6')
g.add_vertex('Q')
g.add_vertex('R')
g.add_vertex('S')
# Add the undirected edges between the vertices
g.add_edge('A', 'TX')
g.add_edge('A', 'E')
g.add_edge('A', 'F')
g.add_edge('TX', 'T1')
g.add_edge('TX', 'F')
g.add_edge('T1', 'D')
g.add_edge('T1', 'G')
g.add_edge('D', 'G')
g.add_edge('D', 'T3')
g.add_edge('E', 'T2')
g.add_edge('E', 'F')
g.add_edge('F', 'T2')
g.add_edge('G', 'T4')
g.add_edge('T3', 'T5')
g.add_edge('J', 'T2')
g.add_edge('J', 'G')
g.add_edge('J', 'T4')
g.add_edge('T4', 'O')
g.add_edge('T4', 'N')
g.add_edge('T5', 'G')
g.add_edge('T5', 'P')
g.add_edge('T2', 'M')
g.add_edge('T2', 'N')
g.add_edge('M', 'N')
g.add_edge('O', 'P')
g.add_edge('T6', 'P')
g.add_edge('T6', 'Q')
g.add_edge('T6', 'R')
g.add_edge('T6', 'S')


test = Graph()
# stores the number of vertices in the graph
test.add_vertex('T0')
test.add_vertex('B')
test.add_vertex('T1')
test.add_vertex('T2')
test.add_vertex('T3')
test.add_vertex('C')
test.add_vertex('D')
test.add_vertex('E')
test.add_vertex('T4')
test.add_vertex('F')
test.add_vertex('G')
test.add_vertex('T5')
test.add_vertex('H')
# Add the undirected edges between the vertices
test.add_edge('T0', 'B')
test.add_edge('T0', 'T1')
test.add_edge('B', 'T2')
test.add_edge('T1', 'T3')
test.add_edge('C', 'T2')
test.add_edge('C', 'D')
test.add_edge('T4', 'D')
test.add_edge('T3', 'E')
test.add_edge('T4', 'F')
test.add_edge('F', 'G')
test.add_edge('G', 'T5')
test.add_edge('H', 'T5')
test.add_edge('H', 'E')


eg = Graph()
# stores the number of vertices in the graph
eg.add_vertex('A')
eg.add_vertex('B')
eg.add_vertex('C')
eg.add_vertex('D')
eg.add_vertex('T1')
eg.add_vertex('F')
eg.add_vertex('G')
eg.add_vertex('T2')
eg.add_vertex('I')

# Add the undirected edges between the vertices
eg.add_edge('A', 'T1')
eg.add_edge('A', 'B')
eg.add_edge('T1', 'F')
eg.add_edge('B', 'C')
eg.add_edge('C', 'D')
eg.add_edge('D', 'T1')
eg.add_edge('T1', 'T2')
eg.add_edge('F', 'T2')
eg.add_edge('F', 'G')
eg.add_edge('T2', 'G')
eg.add_edge('T2', 'I')

eg.print_graph()
print(eg.BFS('T2', 0))