/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    // base case
    if (root == null || root.val == val)
        return root
    // check if val < current val
    if (val < root.val)
    // go to left child
        return searchBST(root.left, val)
    // go to right child
    else
        return searchBST(root.right, val)
};