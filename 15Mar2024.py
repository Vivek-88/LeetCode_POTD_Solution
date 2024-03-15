from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fre = [0]*65
        for num in nums :
            fre[num+30]+=1
        
        for i in range(len(nums)) :
            fre[nums[i]+30]-=1
            ans=1
            for j in range(len(fre)) :
                ans*=pow(j-30,fre[j])
            fre[nums[i]+30]+=1
            nums[i]=ans
        return nums