import java.util.ArrayList;
import java.util.List;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        for (int[] f : flights) {
            graph[f[0]].add(new int[] { f[1], f[2] });
        }

        return f(graph, src, dst, k, new Integer[n][k + 5]);
    }

    public int f(List<int[]>[] graph, int src, int dst, int k, Integer[][] dp) {
        if (k < -1)
            return -1;
        if (src == dst) {
            return 0;
        }
        if (dp[src][k + 1] != null)
            return dp[src][k + 1];
        // System.out.println(src+" "+k);
        int ans = Integer.MAX_VALUE;
        for (int[] e : graph[src]) {
            int f1 = f(graph, e[0], dst, k - 1, dp);
            if (f1 != -1)
                ans = Math.min(ans, f1 + e[1]);
        }
        if (ans == Integer.MAX_VALUE)
            ans = -1;
        return dp[src][k + 1] = ans;
    }
}