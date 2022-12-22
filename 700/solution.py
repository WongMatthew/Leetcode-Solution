# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # base case
        if root is None or root.val == val:
            return root
        # check if val < less than curr val
        if val < root.val:
        # go to left child
            return self.searchBST(root.left, val)
        else:
        # go to right child
            return self.searchBST(root.right, val)