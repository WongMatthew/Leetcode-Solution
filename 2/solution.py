# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1, l2):
    # Initialize variables to keep track of the result and any excess from the previous addition
    result = ListNode(0)
    carry = 0

    # Initialize a pointer to the result linked list and two pointers to the input linked lists
    curr_result = result
    curr_l1 = l1
    curr_l2 = l2

    # Iterate until both input linked lists are empty
    while curr_l1 or curr_l2:
        # Extract the values of the current nodes in the input linked lists, or set them to 0 if the linked list is empty
        val1 = curr_l1.val if curr_l1 else 0
        val2 = curr_l2.val if curr_l2 else 0

        # Add the values and carry from the previous addition
        total = val1 + val2 + carry

        # Update the carry for the next iteration
        carry = total // 10

        # Update the value of the current node in the result linked list
        curr_result.next = ListNode(total % 10)

        # Move the pointers to the next nodes in the input and result linked lists
        curr_result = curr_result.next
        curr_l1 = curr_l1.next if curr_l1 else None
        curr_l2 = curr_l2.next if curr_l2 else None

    # If there is a carry left over, add a new node to the result linked list
    if carry > 0:
        curr_result.next = ListNode(carry)

    # Return the result linked list, starting from the second node (the first node was just a placeholder)
    return result.next