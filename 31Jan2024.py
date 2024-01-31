from ast import List


class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stk = []
        n = len(t)
        ans = [0]*n
        for i in range(n-1,-1,-1) :
            while(len(stk)>0 and t[stk[-1]]<=t[i]) :
                stk.pop()
            if(len(stk)==0) :
                ans[i]=0
            else :
                ans[i]=stk[-1]-i
            stk.append(i)
        return ans