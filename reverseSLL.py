# Reverse a SLL - Time: O(n), space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = None
        while node:
            saving_next_node = node.next
            node.next = prev
            prev = node
            node = saving_next_node
        return prev
         
        