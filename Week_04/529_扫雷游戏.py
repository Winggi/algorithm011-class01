class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if not board: return []
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.m, self.n = len(board), len(board[0])
        self.dfs(board, x, y)
        return board
        
    def dfs(self, board, x, y):
        
        if board[x][y] != 'E': return

        mine_cnt = 0
        for (i, j) in self.directions:
            if 0 <= x + i < self.m and 0 <= y + j < self.n and board[x + i][y + j] == 'M':
                mine_cnt += 1
        if mine_cnt > 0:
            board[x][y] = str(mine_cnt)
        else:  # i.e.,==0
            board[x][y] = 'B'
            for (i, j) in self.directions:
                if 0 <= x + i < self.m and 0 <= y + j < self.n:
                    self.dfs(board, x + i, y + j)