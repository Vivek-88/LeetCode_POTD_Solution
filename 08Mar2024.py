from ast import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fre =[0]*101
        mx=0
        for num in nums :
            fre[num]+=1
            mx = max(mx,fre[num])
        ct=0
        for i in fre :
            if(mx==i) :
                ct+=mx
        return ct