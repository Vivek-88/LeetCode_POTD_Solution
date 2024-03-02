from ast import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        idx=0
        while(idx<len(nums) and nums[idx]<0) :
            idx+=1
        
        list =[]
        jdx=idx-1
        while(idx<len(nums) and jdx>=0) :
            if(-nums[jdx]<nums[idx]) :
                list.append(nums[jdx]*nums[jdx])
                jdx-=1
            else :
                list.append(nums[idx]*nums[idx])
                idx+=1
        while(idx<len(nums)) :
            list.append(nums[idx]*nums[idx])
            idx+=1
        
        while(jdx>=0) :
            list.append(nums[jdx]*nums[jdx])
            jdx-=1
        
        return list