# Unique Paths - Time: O(m*n), Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Return number of unique paths in an m x n grid."""
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
