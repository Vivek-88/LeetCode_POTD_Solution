class Solution {
    public int minSteps(String s, String t) {
        int[] fre = new int[26];
        for (int i = 0; i < s.length(); i++) {
            fre[s.charAt(i) - 'a']++;
            fre[t.charAt(i) - 'a']--;
        }
        int ans = 0;
        for (int f : fre)
            if (f > 0)
                ans += f;
        return ans;
    }
}