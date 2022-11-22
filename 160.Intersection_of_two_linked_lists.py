# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Second solution is better, but difficult to come up with in the interview. So trying an easy solution with
#same complexities
class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:

        curr_a = headA
        len_a = 0
        while curr_a:
            len_a += 1
            curr_a = curr_a.next

        curr_b = headB
        len_b = 0
        while curr_b:
            len_b += 1
            curr_b = curr_b.next

        curr_a = headA
        curr_b = headB
        len_diff = len_a - len_b
        if len_diff > 0:
            curr_a = self.adjust_pointer(curr_a, len_diff)
        else:
            curr_b = self.adjust_pointer(curr_b, abs(len_diff))

        while curr_a:
            if curr_a == curr_b:
                return curr_a
            curr_a = curr_a.next
            curr_b = curr_b.next
        return None

    def adjust_pointer(self, node, n_positions):

        i = 0
        while i < n_positions:
            node = node.next
            i += 1

        return node


'''
# Time - O(m + n) and space - O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        curr_a = headA
        curr_b = headB
        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a else headB
            curr_b = curr_b.next if curr_b else headA
        return curr_a
'''
'''
# Time - O(m + n) and space O(m) or O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        seen = set()

        current = headA
        while current:
            seen.add(current)
            current = current.next
        
        current = headB
        while current:
            if current in seen:
                return current
            current = current.next
            
        return None
'''
