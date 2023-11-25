class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        ans = [0]*n
    
        for i in range(1,n):
            prefix[i] = nums[i]+prefix[i-1]
            suffix[n-i-1] = suffix[n-i]+nums[n-i-1]
        
        for i in range(n):
            ans[i] = (nums[i]*i- prefix[i])+ suffix[i]-(nums[i]*(n-i-1))
        return ans
        