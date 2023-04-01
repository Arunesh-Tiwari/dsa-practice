# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head.next == None):
            return None
        
        count =1 
        aru = head
        
        while(aru.next!= None):
            count+=1
            aru = aru.next
            
        if(count == n):
            return head.next
        
        aru = head
        
        for i in range(count-n-1):
            aru = aru.next
            
        aru.next = aru.next.next
        return head