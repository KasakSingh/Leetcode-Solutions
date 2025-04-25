#LeetCode: https://leetcode.com/problems/reverse-linked-list/submissions/
#Problem: Reversed Linked List


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previous = None
        current = head      
        while current:
            next_node = current.next  
            current.next = previous       
            previous = current       
            current = next_node                  
        return previous 