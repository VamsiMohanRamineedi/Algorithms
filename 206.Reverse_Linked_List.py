# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Recursive solution. Time and space - O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        def helper(prev, curr):

            if not curr:
                return prev

            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
            return helper(prev, curr)

        return helper(prev, curr)


'''
#Iterative solution. Time - O(n) and space - O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
'''
