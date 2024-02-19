import java.util.Arrays;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> (a[0] - b[0]));
        long[][] room = new long[n][2];
        for (int[] meet : meetings) {
            int idx = -1;
            for (int i = 0; i < n; i++) {
                if (room[i][0] <= meet[0]) {
                    idx = i;
                    break;
                } else {
                    if (idx == -1 || room[i][0] < room[idx][0]) {
                        idx = i;
                    }
                }
            }
            // System.out.println(idx);
            room[idx][0] = Math.max(meet[1], room[idx][0] + (long) (meet[1] - meet[0]));
            room[idx][1]++;
        }
        System.out.println(Arrays.deepToString(room));
        int ans = 0;
        for (int i = 1; i < n; i++) {

            if (room[i][1] > room[ans][1])
                ans = i;
        }
        return ans;
    }
}