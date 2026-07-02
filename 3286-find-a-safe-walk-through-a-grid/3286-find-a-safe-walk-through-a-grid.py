from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rowLength = len(grid)
        colLength = len(grid[0])
        
        dRow = [1, -1, 0, 0]
        dCol = [0, 0, -1, 1]
        
        vis = [[-1 for _ in range(colLength)] for _ in range(rowLength)]
        
        def isSafe(row, col, current_health):
            if row < 0 or col < 0 or row >= rowLength or col >= colLength:
                return False
            if current_health < 1 or current_health <= vis[row][col]:
                return False
            return True
        
        q = deque()
        
        start_health = health - grid[0][0]
        q.append((0, 0, start_health))
        vis[0][0] = start_health

        while len(q) > 0:
            x, y, h = q.popleft()
            
            if x == rowLength - 1 and y == colLength - 1 and h >= 1:
                return True
                
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                
                if 0 <= adjx < rowLength and 0 <= adjy < colLength:
                    next_health = h - grid[adjx][adjy]
                    if isSafe(adjx, adjy, next_health):
                        vis[adjx][adjy] = next_health
                        q.append((adjx, adjy, next_health))
                        
        return False