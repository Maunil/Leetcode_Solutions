class Solution:
    def distance_calculate(self, x, y):
        return (x**2 + y**2)
            
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for i in range(len(points)):
            dis = self.distance_calculate(points[i][0], points[i][1])*-1
            if len(heap) < K:
                heapq.heappush(heap, (dis, [points[i][0], points[i][1]]))
            elif heap[0][0] < dis:
                heapq.heapreplace(heap, (dis, [points[i][0], points[i][1]]))        
            
        return [heap[i][1] for i in range (K)]
        
        
        