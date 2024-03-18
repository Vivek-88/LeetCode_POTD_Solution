from ast import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum=0
        mp = {0:-1}
        ans=0
        for i in range(len(nums)) :
            if(nums[i]==0) :
                sum-=1
            else :
                sum+=1
            # print(mp,sum)
            if sum in mp :
                ans = max(ans,i-mp[sum])
            else :
                mp[sum]=i
        return ans
            