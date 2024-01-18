# Problem Link :- https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        list = [0]*(n+5)
        list[n]=1
        for i in range(n-1,-1,-1) :
            list[i]=list[i+1]+list[i+2]
        return list[0]