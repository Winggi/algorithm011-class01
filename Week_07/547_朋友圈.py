class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.n_group = n

            def union(self, i, j):
                a = self.find_parent(i)
                b = self.find_parent(j)
                if a != b:
                    self.parents[a] = b
                    self.n_group -= 1

            def find_parent(self, i):
                root = i
                while self.parents[root] != root:
                    root = self.parents[root]
                while self.parents[i] != i:  # 路径压缩
                    self.parents[i], i = root, self.parents[i] 
                return root

        uf = UnionFind(len(M))
        for i in range(len(M) - 1):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.n_group


        # 法二：DFS
        # visited = set()
        # def dfs(i):
        #     visited.add(i)
        #     for j in range(len(M)):
        #         if M[i][j] == 1:
        #             M[i][j] = 0
        #             M[j][i] = 0
        #             dfs(j)
                    
        # res = 0
        # for i in range(len(M)):
        #     if i not in visited:
        #         dfs(i)
        #         res += 1
        # return res