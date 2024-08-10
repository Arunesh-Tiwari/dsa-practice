# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, cur = None, slow
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        # Step 3: Merge the two halves
        ptr1, ptr2 = head, prev
        while ptr2.next:
            temp1, temp2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1

            ptr1, ptr2 = temp1, temp2
