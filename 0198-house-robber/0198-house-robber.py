class Solution:
    def rob(self, nums: List[int]) -> int:
        c1, c2 = 0,0 
        for i in nums:
            temp = max(i+c1, c2)
            c1 = c2
            c2 = temp
        return c2
        