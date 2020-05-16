"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node 
        
        Q = []
        Q.append(node)
        add_dic = {}
        
        while Q:
            n = Q[0]
            Q.pop(0)
            
            if n.val not in add_dic:    
                temp = Node(n.val)
                temp.neighbors = []
                add_dic[n.val] = temp 
            else:
                temp = add_dic[n.val]
                temp.neighbors = []
                
            for i in range(len(n.neighbors)):
                if n.neighbors[i].val not in add_dic:            
                    t = Node(n.neighbors[i].val)    
                    temp.neighbors.append(t)
                    add_dic[n.neighbors[i].val] = t
                    Q.append(n.neighbors[i])
                else:
                    temp.neighbors.append(add_dic[n.neighbors[i].val])
                                        
                
        return add_dic[1]
        
                
                
            
            
        