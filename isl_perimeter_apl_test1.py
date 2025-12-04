from typing import List

class solv:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    
                    for i_off, j_off in [(0, 1), (1, 0),
                                         (0, -1), (-1, 0)]:
                        r, c = i + i_off, j + j_off
                        
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                            perimeter -= 1
                            
                            
        return perimeter


s = solv()

result = s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])

print(result)