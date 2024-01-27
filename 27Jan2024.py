class Solution:
    def __init__(self):
        self.MOD = int(1e9 + 7)
        self.dp = None

    def kInversePairs(self, n, k):
        self.dp = [[None] * (k + 1) for _ in range(n + 1)]
        return self.getInversions(n, k)

    def getInversions(self, n, k):
        if n == 0:
            return 0

        if k == 0:
            return 1

        if self.dp[n][k] is not None:
            return self.dp[n][k]

        result = 0

        for inversion in range(min(k, n)):
            result += self.getInversions(n - 1, k - inversion)
            result %= self.MOD

        self.dp[n][k] = result
        return result
