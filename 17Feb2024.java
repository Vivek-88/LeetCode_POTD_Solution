import java.util.Arrays;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        int[][] a = new int[heights.length][2];
        for (int i = 0; i < heights.length - 1; i++) {
            a[i][0] = Math.max(0, heights[i + 1] - heights[i]);
            a[i][1] = i + 1;
        }
        Arrays.sort(a, (b, c) -> b[0] - c[0]);
        int lo = 0, hi = heights.length - 1;
        int ans = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int b = bricks, l = ladders;
            for (int i = 0; i < a.length; i++) {
                if (a[i][1] <= mid) {
                    if (b >= a[i][0]) {
                        b -= a[i][0];
                    } else {
                        l--;
                    }
                }
            }

            if (b >= 0 && l >= 0) {
                ans = Math.max(ans, mid);
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
}