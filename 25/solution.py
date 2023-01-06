# beats 63% runtime and 55% memory

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: 
            return head

        slow, fast, temp = head, head, []
        
        while fast:
            temp.append(fast.val)
            
            if len(temp) == k:
                while temp:
                    slow.val = temp.pop()
                    slow = slow.next
                    
            fast = fast.next
            
        return head