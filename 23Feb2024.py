from ast import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f in flights:
            graph[f[0]].append([f[1], f[2]])

        return self.f(graph, src, dst, k, [[None] * (k + 5) for _ in range(n)])

    def f(self, graph, src, dst, k, dp):
        if k < -1:
            return -1
        if src == dst:
            return 0
        if dp[src][k + 1] is not None:
            return dp[src][k + 1]

        ans = float('inf')
        for e in graph[src]:
            f1 = self.f(graph, e[0], dst, k - 1, dp)
            if f1 != -1:
                ans = min(ans, f1 + e[1])

        if ans == float('inf'):
            ans = -1
        dp[src][k + 1] = ans
        return ans
        