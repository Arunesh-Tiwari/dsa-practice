from heapq import heappush, heappop

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nums, temp = [], head
        
        while temp != None:
            heappush(nums, temp.val)
            temp = temp.next
        
        nums = [heappop(nums) for i in range(len(nums))]
        
        if len(nums) == 0:
            return None
        
        newList = ListNode(nums[0])
        temp = newList
        
        for n in nums[1:]:
            t = ListNode(n)
            temp.next = t
            temp = temp.next
        
        return newList