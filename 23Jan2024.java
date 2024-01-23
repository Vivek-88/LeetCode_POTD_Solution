import java.util.List;

class Solution {
    public int maxLength(List<String> arr) {
        int ans = 0;
        for (int i = 1; i < (1 << arr.size()); i++) {
            boolean isValid = true;
            int l = 0;
            int[] fre = new int[26];
            for (int j = 0; j < arr.size() && isValid; j++) {
                if ((i & (1 << j)) != 0) {
                    for (int k = 0; k < arr.get(j).length(); k++) {
                        if (fre[arr.get(j).charAt(k) - 'a'] > 0)
                            isValid = false;
                        fre[arr.get(j).charAt(k) - 'a']++;
                    }
                    // System.out.println()
                    l += arr.get(j).length();
                }
            }
            // System.out.println(i+" "+l+" "+isValid);
            if (isValid)
                ans = Math.max(ans, l);
        }
        return ans;
    }
}