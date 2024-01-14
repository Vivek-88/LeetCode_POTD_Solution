import java.util.Arrays;

class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length())
            return false;
        int[] fre1 = new int[26];
        int[] fre2 = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            fre1[word1.charAt(i) - 'a']++;
            fre2[word2.charAt(i) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (fre1[i] != fre2[i]) {
                if (fre1[i] == 0 || fre2[i] == 0)
                    return false;
            } else {
                fre1[i] = fre2[i] = -1;
            }
        }

        Arrays.sort(fre1);
        Arrays.sort(fre2);
        int ct = 0;
        for (int i = 0; i < 26; i++) {
            if (fre1[i] != fre2[i]) {
                return false;
            } else {
                ct++;
            }
        }
        if (ct % 2 == 1)
            return false;
        return true;

    }
}