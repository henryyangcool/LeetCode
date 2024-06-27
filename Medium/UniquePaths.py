class Solution:
    def uniquePaths(self, m, n):
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or (i == 0 and j != 0) or (i != 0 and j == 0):
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[m - 1][n - 1]
