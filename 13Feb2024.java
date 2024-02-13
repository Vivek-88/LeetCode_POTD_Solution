class Solution {
    public String firstPalindrome(String[] words) {
        for (String s : words) {
            boolean isValid = true;
            for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
                if (s.charAt(i) != s.charAt(j)) {
                    isValid = false;
                }
            }
            if (isValid)
                return s;
        }
        return "";
    }
}