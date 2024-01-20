# Problem Link :- https://leetcode.com/problems/sum-of-subarray-minimums/

from ast import List


class Solution:
    mod = 1000000007
    def add(self,a:int,b:int) :
        return (a+b)%self.mod
    
    def sub(self,a:int,b:int) :
        return (a-b+self.mod)%self.mod
    
    def multi(self,a:int,b:int) :
        return (a*b)%self.mod
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk = [0]
        n = len(arr)
        left = [0]*n
        
        for i in range(0,n) :
            while(len(stk)>0 and arr[i]<=arr[stk[-1]]) :
                stk.pop()
            if(len(stk)==0) :
                left[i]=-1
            else :
                left[i]=stk[-1]
            stk.append(i)
        
        right = [0]*n
        stk.clear()
        
        for i in range(n-1,-1,-1) :
            while(len(stk)>0 and arr[i]<arr[stk[-1]]) :
                stk.pop()
            if(len(stk)==0) :
                right[i]=n
            else :
                right[i]=stk[-1]
            stk.append(i)
        
        # print(left,"",right)
        
        ans=0
        for i in range(n) :
            val = self.multi(self.sub(right[i],i),self.sub(i,left[i]))
            val = self.multi(val,arr[i])
            ans = self.add(ans,val)
        return ans