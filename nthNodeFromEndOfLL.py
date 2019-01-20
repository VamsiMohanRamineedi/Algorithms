# Remove nth-node from the end of linked list
# Time complexity: O(length), space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
    
        nStepsForward = head
        node = head        
        for i in range(0,n):
            nStepsForward = nStepsForward.next
        # if n = length of LL, head needs to be removed
        if nStepsForward == None:
            return head.next
        while nStepsForward.next:
            nStepsForward = nStepsForward.next
            node = node.next
        node.next = node.next.next
        return head