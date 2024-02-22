from ast import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [[0]*2 for _ in range(n+1)]
        for t in trust :
            a[t[1]][0]+=1
            a[t[0]][1]=1
        
        for i in range(1,n+1) :
            if(a[i][0]==n-1 and a[i][1]==0) :
                return i
        return -1