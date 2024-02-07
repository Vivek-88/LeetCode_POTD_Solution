import java.util.Arrays;

class Solution {
    public String frequencySort(String s) {
        int[][] fre = new int[62][2];
        for (int i = 0; i < 62; i++)
            fre[i][1] = i;
        for (int i = 0; i < s.length(); i++)
            fre[idx(s.charAt(i))][0]++;
        Arrays.sort(fre, (a, b) -> (a[0] == b[0]) ? b[1] - a[1] : b[0] - a[0]);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 62; i++) {
            // System.out.println(fre[i][0]);
            while (fre[i][0]-- > 0) {
                sb.append(chr(fre[i][1]));
            }
        }
        return sb.toString();
    }

    public int idx(char c) {
        // System.out.println(c);
        if (c >= 'a')
            return c - 'a' + 36;
        if (c >= 'A')
            return c - 'A' + 10;
        return c - '0';
    }

    public char chr(int i) {
        if (i >= 36)
            return (char) (i - 36 + 'a');
        if (i >= 10)
            return (char) (i - 10 + 'A');
        return (char) (i + '0');
    }
}