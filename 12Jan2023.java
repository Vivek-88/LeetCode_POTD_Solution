class Solution {
    public boolean halvesAreAlike(String s) {
        int f1 = 0, f2 = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s.charAt(i))) {
                if (i < s.length() / 2) {
                    f1++;
                } else {
                    f2++;
                }
            }
        }
        return f1 == f2;

    }

    public boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O'
                || c == 'U';
    }
}