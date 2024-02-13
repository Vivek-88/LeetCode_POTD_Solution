from ast import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            is_valid = True
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    is_valid = False
                    break
            if is_valid:
                return s
        return ""