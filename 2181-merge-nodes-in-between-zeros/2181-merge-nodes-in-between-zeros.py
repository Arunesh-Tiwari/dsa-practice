# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

		curr = head.next
		res = new_node = ListNode(0)

		while curr:
			sum = 0
			while curr.val != 0:
				sum += curr.val
				curr = curr.next
			new_node.next = ListNode(sum)
			new_node = new_node.next
			curr = curr.next

		return res.next
