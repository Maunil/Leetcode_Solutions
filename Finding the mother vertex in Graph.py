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

  def DFS_util (self, visit, node_key):
    if node_key in self.G and visit[node_key] == False:
      for i in range(len(self.G[node_key])):
        self.DFS_util(visit, self.G[node_key][i])
        visit[self.G[node_key][i]] = True

  def DFS_traverse(self):
    visit = [False]*self.n

    for i in range(self.n):
      if visit[i] == False:
        self.DFS_util(visit, i)
        mother_index = i
        visit[i] = True

    visit = [False]*self.n
    self.DFS_util(visit, mother_index)
    visit[mother_index] = True

    if  self.check_visited(visit):
      return mother_index

    return -1 

  def check_visited(self, visit):
    for i in range(len(visit)):
      if visit[i] == False:
        return False
      
    return True
    
g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(3,0)
g.add_edge(3,1)
g.add_edge(3,4)
g.add_edge(4,1)


print ("This Graph structure is : " + str(g.G))
print ("The mother vertex is : " + str(g.DFS_traverse()))
