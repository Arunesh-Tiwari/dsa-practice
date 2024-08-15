class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        if len(nums) < 2:
            return index
        
        else:

            for i in range(2, len(nums)):
                if nums[i] != nums[index-2]:
                    nums[index] = nums[i]
                    index += 1
            return index



                
            

        