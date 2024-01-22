# Jai Shree Ram
# Problem Link :- https://leetcode.com/problems/set-mismatch/

from ast import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        st = set()
        ans= [0]*2
        for num in nums :
            if(num in st) :
                ans[0]=num
            st.add(num)
        for i in range(1,len(nums)+1) :
            if(i not in st) :
                ans[1]=i
        return ans