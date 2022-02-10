# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
    Given the root of a binary tree, invert the tree, and return its root.
"""
class Solution:
    def invertTree(self, root:[TreeNode]) ->[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    print("LeetCode Problem: 226. Invert Binary Tree")
    root = TreeNode(3,TreeNode(4,TreeNode(1,None, None),TreeNode(2,None, None)),TreeNode(5,None,None))
    print("root: [",root.val,",",root.left.val,",",root.right.val, ",", root.left.left.val,",",root.left.right.val,",",root.right.val,"]")
    solution = Solution()
    result = solution.invertTree(root)
    print("result: [", result.val, ",", result.left.val, ",", result.right.val, ",", result.right.left.val, ",",result.right.right.val, ",", result.left.val, "]")


