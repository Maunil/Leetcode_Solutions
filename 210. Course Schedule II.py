class Solution:
    def dfs_util(self, G, course, ans, visit, path_ancestors):
        if course in path_ancestors:
            return False 
                
        path_ancestors [course] = True 
        for i in range(len(G[course])):
            if visit[G[course][i]] == False:
                if self.dfs_util(G, G[course][i], ans, visit, path_ancestors):
                    visit[G[course][i]] = True 
                else:
                    return False 
                
        del path_ancestors[course]
        ans.append(course)
        return True 
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = {}
        visit = []
        ans = []
        for i in range(numCourses):
            G[i] = []
            visit.append(False) 
                
        for i in range(len(prerequisites)):
            G[prerequisites[i][0]].append(prerequisites[i][1])
        
        for i in range(numCourses):
            if visit[i] == False:
                if self.dfs_util(G, i, ans, visit, {}):    
                    visit[i] = True 
                else:
                    return [] 
        return ans 