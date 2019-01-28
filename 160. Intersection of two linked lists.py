# Intersection of two linked lists - Time: O(m+n), space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        result = None
        node_a = headA
        # find a's tail
        while node_a.next:
            node_a = node_a.next
        node_a.next = headB # make a's tail point to b's head, this forms a circular linkedlist 
        
        slow = headA
        fast = headA
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                result = slow
                break
        # remove the connection 
        node_a.next = None
        return result
