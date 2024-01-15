import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> map2 = new HashMap<>();

        for (int[] m : matches) {
            map1.put(m[0], map2.getOrDefault(m[0], 0) + 1);
            map2.put(m[1], map2.getOrDefault(m[1], 0) + 1);
        }

        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>());
        ans.add(new ArrayList<>());

        for (int key : map1.keySet()) {
            if (!map2.containsKey(key)) {
                ans.get(0).add(key);
            }
        }

        for (int key : map2.keySet()) {
            if (map2.get(key) == 1)
                ans.get(1).add(key);
        }
        Collections.sort(ans.get(0));
        Collections.sort(ans.get(1));

        return ans;
    }
}