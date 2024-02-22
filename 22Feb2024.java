class Solution {
    public int findJudge(int n, int[][] trust) {
        int[][] a = new int[n + 1][2];
        for (int[] t : trust) {
            a[t[1]][0]++;
            a[t[0]][1] = 1;
        }

        for (int i = 1; i <= n; i++)
            if (a[i][0] == n - 1 && a[i][1] == 0)
                return i;
        return -1;
    }
}