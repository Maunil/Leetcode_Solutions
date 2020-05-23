# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def creating_graph_from_tree(self, root, Graph):
        if root :
            if root not in Graph:
                Graph[root] = []
            
            if root.left:
                Graph[root].append(root.left)
                Graph[root.left] = []
                Graph[root.left].append(root) 
                self.creating_graph_from_tree(root.left, Graph)
            
            if root.right:
                Graph[root].append(root.right)
                Graph[root.right] = []
                Graph[root.right].append(root) 
                self.creating_graph_from_tree(root.right, Graph)
        
    def BFS_helper(self, target, Graph, K, ans):
        Q = []
        visited = {}
        Q.append(target)
        visited[target] = True 
        while Q:
            n = len(Q)
            while n: 
                node = Q[0]
                for i in range(len(Graph[node])):
                    if Graph[node][i] not in visited:
                        Q.append(Graph[node][i])
                        visited[Graph[node][i]] = True 
                        
                Q.pop(0)
                n = n - 1 
            K = K - 1 
            
            if K == 0:
                while Q:
                    ans.append(Q[0].val)
                    Q.pop(0)
                return 
            
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        Graph = {}
        ans = []
        self.creating_graph_from_tree(root, Graph)
        if K == 0:
            return [target.val]        
        if target not in Graph:
            return ans 
        self.BFS_helper(target, Graph, K, ans)
        return ans 
        
        
        