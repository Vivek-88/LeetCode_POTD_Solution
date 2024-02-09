from ast import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxi = 1
        num = -1
        v = []
        nums.sort()
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    if maxi < dp[i]:
                        maxi = dp[i]

        for i in range(n - 1, -1, -1):
            if maxi == dp[i] and (num == -1 or (num % nums[i]) == 0):
                v.append(nums[i])
                maxi -= 1
                num = nums[i]

        return v