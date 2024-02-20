class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n = (n*(n+1))//2
        for num in nums :
            n-=num
        return n