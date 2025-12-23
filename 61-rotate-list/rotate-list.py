# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        # Step 1: find length and tail
        curr = head
        length = 1
        while curr.next is not None:
            curr = curr.next
            length += 1

        # Step 2: make circular
        curr.next = head

        # Step 3: effective rotation
        k = k % length
        steps = length - k

        # Step 4: find new tail
        curr_n = head
        for _ in range(steps - 1):
            curr_n = curr_n.next

        # Step 5: break circle
        newhead = curr_n.next
        curr_n.next = None

        return newhead

    

        
        
    

        