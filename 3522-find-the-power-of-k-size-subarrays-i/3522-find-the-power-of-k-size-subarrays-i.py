from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        is_valid = True
        
        
        for i in range(1, k):
            if nums[i] != nums[i-1] + 1:
                is_valid = False
                break
        results.append(max(nums[:k]) if is_valid else -1)
        
        for i in range(1, n - k + 1):
            if is_valid and nums[i + k - 1] == nums[i + k - 2] + 1:
                results.append(max(nums[i:i + k]))
            else:
                is_valid = True
                for j in range(i + 1, i + k):
                    if nums[j] != nums[j-1] + 1:
                        is_valid = False
                        break
                results.append(max(nums[i:i + k]) if is_valid else -1)
        
        return results
