class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=nums[0]
        Sum = nums[0]
        
        for i in range(1,len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])
            Sum = max(cur_sum, Sum)
        return Sum