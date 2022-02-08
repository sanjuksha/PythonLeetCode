# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        Given the roots of two binary trees p and q,
        this function checks if they are the same or not.
        Two binary trees are considered the same if they are structurally identical,
         and the nodes have the same value.
    """
    def isSameTree(self, p:[TreeNode], q:[TreeNode]) -> bool:
        #Check if both trees are null tree
        if not p and not q:
            return True
        #Check if one of them is null
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


if __name__ == '__main__':
    print("LeetCode Problem: 100. Same Tree")
    p = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
    q = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
    solution = Solution()
    result = solution.isSameTree(p,q)
    print(result)