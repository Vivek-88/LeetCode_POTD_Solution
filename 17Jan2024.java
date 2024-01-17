import java.util.Arrays;

class Solution {
    public boolean uniqueOccurrences(int[] nums) {
        int[] fre = new int[2005];
        for (int num : nums)
            fre[num + 1000]++;
        Arrays.sort(fre);
        for (int i = 0; i < 2004; i++) {
            if (fre[i] == 0)
                continue;
            if (fre[i] == fre[i + 1])
                return false;
        }
        return true;
    }
}