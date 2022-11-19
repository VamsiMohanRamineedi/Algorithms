# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time - O(n) and space - O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # slow finds middle node
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None
        reversed_second_head = self.reverse_linked_list(second_head)

        current_second_head = reversed_second_head
        current_first_head = head
        result = True
        while result and current_second_head:
            if current_second_head.val != current_first_head.val:
                result = False
            current_second_head = current_second_head.next
            current_first_head = current_first_head.next

        second_head = self.reverse_linked_list(reversed_second_head)
        slow.next = second_head

        return result

    def reverse_linked_list(self,
                            head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


'''
#Created another member variable called prev. Could be O(n) because of that
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        prev = None
        current = head
        while current:
            current.prev = prev
            prev = current
            current = current.next
        
        tail = prev
        normal = head
        reverse = tail

        while normal and normal != reverse and normal.prev != reverse:
            if normal.val != reverse.val:
                return False
            normal = normal.next
            reverse = reverse.prev

        return True
'''
'''
# Time and space: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        list_nums = []
        current = head

        while current:
            list_nums.append(current.val)
            current = current.next
        
        left = 0
        right = len(list_nums) - 1

        while left < right:
            if list_nums[left] != list_nums[right]:
                return False
            left += 1
            right -= 1
        
        return True
'''
