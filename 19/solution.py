#beats 90% of runtime and 17% of memory


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy head, when right is 0
        dummy = ListNode()
        dummy.next = head
        
        # find len(list) to find distance from right
        length,temp = 0,dummy
        
        while temp is not None:
            length += 1
            temp = temp.next
        right  = length - n
        
        # find the parent of the removing node
        temp = dummy
        while right > 1:
            temp = temp.next
            right -= 1
        
        # remove the node 
        temp.next = temp.next.next
        
        # return the original head
        return dummy.next