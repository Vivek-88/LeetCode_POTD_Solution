import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] c = strs[i].toCharArray();
            Arrays.sort(c);
            String s = new String(c);
            List<String> list = map.getOrDefault(s, new ArrayList<>());
            list.add(strs[i]);
            map.put(s, list);
        }
        List<List<String>> ans = new ArrayList<>();
        for (String key : map.keySet())
            ans.add(map.get(key));
        return ans;
    }
}