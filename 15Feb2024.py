from ast import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans,sum=-1,nums[0]+nums[1]
        for i in range(2,len(nums)) :
            if(nums[i]<sum) :
                ans=max(ans,sum+nums[i])
            sum+=nums[i]
        
        return ans