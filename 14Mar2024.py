from ast import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans=0
        sum = [0]*len(nums)
        sum[0]=nums[0]
        for i in range(1,len(nums)) :
            sum[i] = sum[i-1]+nums[i]
        for i in range(0,len(nums)) :
            lo=i
            hi=len(nums)-1
            j=hi+1
            while(lo<=hi) :
                mid = lo+(hi-lo)//2
                if(sum[mid]-sum[i]+nums[i]<goal) :
                    lo=mid+1
                elif(sum[mid]-sum[i]+nums[i]==goal) :
                    j=min(j,mid)
                    hi=mid-1
                else :
                    hi=mid-1
            lo=i
            hi=len(nums)-1
            k=i
            while(lo<=hi) :
                mid = lo+(hi-lo)//2
                if(sum[mid]-sum[i]+nums[i]<goal) :
                    lo=mid+1
                elif(sum[mid]-sum[i]+nums[i]==goal) :
                    k=max(k,mid)
                    lo=mid+1
                else :
                    hi=mid-1
            if(j<=k) :
                ans+=(k-j+1)
            # print(i,j,k)
        return ans