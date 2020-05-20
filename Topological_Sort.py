'''
Not a leetcode question, time complexity : O (V+E) 
'''
class Graph:
  n = None
  G = None 
  
  def __init__(self, number_of_nodes):
    self.n = number_of_nodes
    self.G = {}
    for i in range(number_of_nodes):
      self.G[i] = []

  def add_edge(self, start, end):
    if start in self.G and end < self.n:
       self.G[start].append(end)

  def DFS_util(self, vertex, S, visited):
    for i in range(len(self.G[vertex])):
      if visited[self.G[vertex][i]] == False:
        visited[self.G[vertex][i]] = True 
        self.DFS_util(self.G[vertex][i], S, visited)
        S.append(self.G[vertex][i])

  def topological_sort(self):
    S = []  # A Stack to keep the ordering
    visited = [False]*self.n # To keep track of the visited nodes 

    for i in range(self.n):
      if visited[i] == False:
        visited[i] = True
        self.DFS_util(i, S, visited)
        S.append(i) 

    # Printing the elements in a reverse order 
    while len(S)>0:
      print (S[-1], end= " ")
      S.pop() 


g = Graph(6)
g.add_edge(0,1)
g.add_edge(0,5)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(5,1)
g.add_edge(5,2)



# g = Graph(8)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(3,4)
# g.add_edge(3,5)
# g.add_edge(5,6)
# g.add_edge(6,7)
# g.add_edge(6,2)
# g.add_edge(7,3)


print ("This Graph structure is : " + str(g.G))
g.topological_sort()