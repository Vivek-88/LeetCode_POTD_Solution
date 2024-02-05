class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre = [0]*26
        for i in range(len(s)) :
            fre[ord(s[i])-ord('a')]+=1
        for i in range(len(s)) :
            if(fre[ord(s[i])-ord('a')]==1) :
                return i
        return -1