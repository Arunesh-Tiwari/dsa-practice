class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<4:
            return sum(nums)
        ans=0
        diff=10000
        nums.sort()
        for i in range(len(nums)-1):
            l,r=i+1,len(nums)-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ==target:
                    return summ
                if abs(summ-target)<diff:
                    diff=abs(summ-target)
                    ans=summ
                if summ<target:
                    l+=1
                if summ>target:
                    r-=1
        return ans