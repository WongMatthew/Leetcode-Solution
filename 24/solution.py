# beats 33% runtime and 59% memory

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head

        prev = None
        cur = head
        ans = head.next
        while cur and cur.next:
            adj = cur.next
            if prev: prev.next = adj

            cur.next, adj.next = adj.next, cur
            prev, cur = cur, cur.next

        return ans or head