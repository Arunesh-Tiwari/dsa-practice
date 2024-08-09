class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) -1
        max_= 0
        while p1 < p2:
            heights = min(height[p1],height[p2])
            weight = p2 - p1 
            container = heights*weight
            max_ = max(max_,container)
            if height[p1] <= height[p2]:
                p1 +=1
            else:
                p2 -=1
        return max_