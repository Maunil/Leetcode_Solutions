class Solution:
    def help (self, M , visited, q):
        while len(q) > 0:
            for i in range(len(M)):
                if M[q[0]][i] == 1 and visited[i] == False:
                    visited[i] = True 
                    q.append (i)
            q.pop(0)
                        
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        q = []
        ans = 0 
        visited = []
        
        for i in range(len(M)):
            visited.append(False)
            
        for i in range(len(M)):
            if visited[i] == False:
                ans = ans + 1 
                visited[i] = True
                q.append(i) 
                self.help(M, visited, q)
                                
        return ans 
        
        
        
        