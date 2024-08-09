class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        low = 0
        high = len(height)-1
        value, maxval = 0, 0
        while low<high:
            value = min(height[low],height[high])*(high-low)
            maxval = max(maxval,value)
            if height[low]<= height[high]:
                low+=1
            else:
                high-=1 
        return maxval
 
