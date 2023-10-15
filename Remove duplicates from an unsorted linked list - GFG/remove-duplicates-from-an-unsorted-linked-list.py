#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    # Function to remove duplicates from an unsorted linked list.
    def removeDuplicates(self, head):
        # Create a set to store unique values.
        unique_values = set()

        # Initialize a pointer to the head of the linked list.
        current = head

        # If the linked list is empty or contains only one node, return as there are no duplicates to remove.
        if not current or not current.next:
            return head

        # Traverse the linked list and keep track of the previous node.
        prev = None

        while current:
            # If the current node's data is not in the set of unique values, add it to the set and move to the next node.
            if current.data not in unique_values:
                unique_values.add(current.data)
                prev = current
                current = current.next
            else:
                # If the current node's data is in the set, skip the current node by updating the previous node's next pointer.
                prev.next = current.next
                current = current.next

        return head  # Return the head of the modified linked list.

            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        a.head = Solution().removeDuplicates(a.head)
        a.printList()
# } Driver Code Ends