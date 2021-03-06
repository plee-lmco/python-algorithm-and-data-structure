# 938. Range Sum of BST easy
# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
#
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#
#
# Note:
#
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    self.results = 0
    # self.recursive(root, L, R)
    # return self.results

    self.iterative(root, L, R)
    return self.results


def recursive(self, root: TreeNode, L: int, R: int) -> int:
    if root == None:
        return

    if L <= root.val <= R:
        self.results += root.val

    self.recursive(root.left, L, R)
    self.recursive(root.right, L, R)


def iterative(self, root: TreeNode, L: int, R: int) -> int:
    stack = [root]

    while (len(stack) != 0):
        node = stack.pop()

        if L <= node.val <= R:
            self.results += node.val

        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)