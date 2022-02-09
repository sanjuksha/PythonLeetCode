# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
    Given the roots of two binary trees root and subRoot, 
    return true if there is a subtree of root with the 
    same structure and node values of subRoot and false otherwise.
    
    A subtree of a binary tree tree is a tree that consists 
    of a node in tree and all of this node's descendants. 
    The tree tree could also be considered as a subtree of itself.
"""
class Solution:
    def isSubtree(self, root:[TreeNode], subRoot:[TreeNode]) -> bool:
        # Check if subroot is a null tree
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root,subRoot):
            return True

        # Either left subtree is equal or right is
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        # Check if both trees are null tree
        if not p and not q:
            return True
        # Check if both trees exist and there root values are same
        # if yes we check if the right and left nodes/trees are same
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

        return False


if __name__ == '__main__':
    print("LeetCode Problem: 572. Sub Tree of Another Tree")
    root = TreeNode(3,TreeNode(4,TreeNode(1,None, None),TreeNode(2,None, None)),TreeNode(5,None,None))
    subroot = TreeNode(4,TreeNode(1,None,None),TreeNode(2,None,None))
    solution = Solution()
    result = solution.isSubtree(root, subroot)
    print(result)