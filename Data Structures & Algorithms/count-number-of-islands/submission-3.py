class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        found = set()
        res = 0

        def dfs(r, c):
            found.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and (nr, nc) not in found and grid[nr][nc] == "1":
                    dfs(nr, nc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in found:
                    res += 1
                    dfs(int(r), int(c))
        return res