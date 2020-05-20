'''
Not a leetcode question, time complexity : O (V+E) 
'''


class Graph:
  n = None
  G = None 
  cycle = None
  def __init__(self, number_of_nodes):
    self.n = number_of_nodes
    self.G = {}
    self.cycle = False
    for i in range(number_of_nodes):
      self.G[i] = []

  def add_edge(self, start, end):
    if start in self.G and end < self.n:
       self.G[start].append(end)

  def cycle_dfs(self, visit, parent_dic, vertex):
    for i in range(len(self.G[vertex])):
      if self.G[vertex][i] in parent_dic:
        self.cycle = True

      elif visit[self.G[vertex][i]] == False:
        visit[self.G[vertex][i]] = True 
        parent_dic[self.G[vertex][i]] = True
        self.cycle_dfs(visit, parent_dic, self.G[vertex][i]) 
        del parent_dic[self.G[vertex][i]]

  def check_cycle(self):
    parent_dic = {}
    visit = [False]*self.n

    for i in range(self.n):
      if visit[i] == False:
        visit[i] = True
        parent_dic[i] = True
        self.cycle_dfs(visit, parent_dic, i)


g = Graph(8)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(5,6)
g.add_edge(6,7)
g.add_edge(6,2)
g.add_edge(7,3)


print ("This Graph structure is : " + str(g.G))
g.check_cycle()

if g.cycle:
  print ("The Graph has cycle")
else:
  print ("The Graph is acyclic")

