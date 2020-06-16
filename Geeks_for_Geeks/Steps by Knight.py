#User function Template for python3
def position_valid (r,c,N,visit):
    if r < 1 or c < 1 or r > N or c > N or visit[r][c] == True:
        return False 
    
    return True 

def knight_steps(r, c, N, Q, visit):
    if position_valid(r+1, c+2, N, visit):
        Q.append([r+1, c+2])
        visit[r+1][c+2] = True
    
    if position_valid(r+1, c-2, N, visit):
        Q.append([r+1, c-2])
        visit[r+1][c-2] = True
    if position_valid(r+2, c+1, N, visit):
        Q.append([r+2, c+1])
        visit[r+2][c+1] = True
        
    if position_valid(r+2, c-1, N, visit):
        Q.append([r+2, c-1])
        visit[r+2][c-1] = True
    
    if position_valid(r-1, c+2, N, visit):
        Q.append([r-1, c+2])
        visit[r-1][c+2] = True
        
    if position_valid(r-1, c-2, N, visit):
        Q.append([r-1, c-2])
        visit[r-1][c-2] = True
        
    if position_valid(r-2, c+1, N, visit):
        Q.append([r-2, c+1])
        visit[r-2][c+1] = True
    
    if position_valid(r-2, c-1, N, visit):
        Q.append([r-2, c-1])
        visit[r-2][c-1] = True
    
def bfs_util(pos, target, N):
    Q = []
    Q.append([pos[0], pos[1]])
    level = 0 
    
    visit = []
    for i in range(N+1):
        visit.append([False for i in range(N+1)])
    
    visit[pos[0]][pos[1]] = True
    
    while Q:
        n = len(Q)
        
        while n:
            p_r, p_c = Q[0]
            Q.pop(0)  
            if p_r == target[0] and p_c == target[1]:
                return level 
            knight_steps (p_r, p_c, N, Q, visit)
            n = n - 1
        
        level += 1 

    return 

def minStepToReachTarget(knightpos, targetpos, N):
    '''
    knightpos: (x,y) tuple of current position coordinate
    targetpos: (x,y) tuple of target position coordinate 
    N: size of board
    
    return: minimum steps the Knight will take to reach the target position
    '''
    
    return bfs_util(knightpos, targetpos, N)
    
    

