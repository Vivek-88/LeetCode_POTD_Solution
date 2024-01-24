from ast import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        fre = [0]*26
        for i in range(1, (1 << len(arr))):
            isValid = True
            l = 0
            for j in range(0,26) :
                fre[j]=0
            for j in range(len(arr)):
                if (i & (1 << j)) != 0:
                    for k in range(len(arr[j])):
                        if fre[ord(arr[j][k]) - ord('a')] > 0:
                            isValid = False
                        fre[ord(arr[j][k]) - ord('a')] += 1
                    l += len(arr[j])
            if isValid:
                ans = max(ans, l)
        return ans