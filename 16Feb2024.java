import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int a : arr)
            map.put(a, map.getOrDefault(a, 0) + 1);
        int[] fre = new int[map.size()];
        int i = 0;
        for (int key : map.keySet()) {
            fre[i] = map.get(key);
            i++;
        }
        Arrays.sort(fre);
        int ans = 0;
        for (i = 0; i < fre.length; i++) {
            if (k >= fre[i]) {
                k -= fre[i];
            } else {
                ans++;
            }
        }
        return ans;
    }
}