class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = []; high = []; eq = []
        for i in range(len(nums)):
            if nums[i]>pivot:
                high.append(nums[i])
            elif nums[i]<pivot:
                low.append(nums[i])
            else:
                eq.append(nums[i])
        return low+eq+high