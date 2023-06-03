class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        dicts = defaultdict(int)
        
        for element in nums:
            dicts[element % space] += 1
            
        target = max(dicts.values())
        
        for element in nums:
            if dicts[element % space] == target:
                return element