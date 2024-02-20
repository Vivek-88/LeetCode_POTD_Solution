class Solution {
    public int idx(char c) {
        if (c >= 'a') {
            return c - 'a' + 26;
        }
        return c - 'A';
    }

    public String minWindow(String s, String t) {
        int[] fre = new int[52];
        for (int i = 0; i < t.length(); i++)
            fre[idx(t.charAt(i))]--;
        int strt = 0, end = 0;
        int i = 0, j = 0, ans = Integer.MAX_VALUE;
        while (j < s.length()) {
            boolean isValid = true;
            for (int f : fre)
                if (f < 0)
                    isValid = false;
            // System.out.println(i+" "+j+" "+Arrays.toString(fre));
            if (isValid) {
                fre[idx(s.charAt(i))]--;
                if (ans > j - i) {
                    ans = j - i;
                    strt = i;
                    end = j;
                }
                i++;
            } else {
                fre[idx(s.charAt(j))]++;
                j++;
            }
        }

        while (i < s.length()) {
            boolean isValid = true;
            for (int f : fre)
                if (f < 0)
                    isValid = false;
            // System.out.println(i+" "+j+" "+Arrays.toString(fre));
            if (isValid) {
                fre[idx(s.charAt(i))]--;
                if (ans > j - i) {
                    ans = j - i;
                    strt = i;
                    end = j;
                }
                i++;
            } else {
                break;
            }
        }
        // System.out.println(ans);
        return s.substring(strt, end);
    }
}