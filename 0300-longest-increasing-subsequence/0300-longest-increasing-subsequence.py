class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = 1

        for i in range(1,n):
            curr_el = nums[i]
            j = i-1
            Max = 0
            while j>=0:
                if nums[j]<curr_el:
                    Max = max(Max,dp[j])
                j -= 1
            dp[i] = 1+Max
        return max(dp)