class Solution:
    def help(self, graph, ans, node_index, curr):
        if node_index == len(graph) - 1:
            curr.append (node_index)
            ans.append(list(curr))
            curr.pop()
            return 
                    
        for i in range(len(graph[node_index])):
            curr.append (node_index)
            self.help(graph, ans, graph[node_index][i], curr)
            curr.pop() 
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for i in range(len(graph[0])):
            self.help(graph, ans, graph[0][i], [0])
        
        return ans 