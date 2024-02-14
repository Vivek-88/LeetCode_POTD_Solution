from ast import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        j,k=0,0
        for i in range(n) :
            if(i%2==0) :
                while(j<n and nums[j]<0) :
                    j+=1
                ans[i]=nums[j]
                j+=1
            else :
                while(k<n and nums[k]>0) :
                    k+=1
                ans[i]=nums[k]
                k+=1
        
        return ans