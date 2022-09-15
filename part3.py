class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeSum:
    def maxPathSum(self, root: TreeNode) -> int:
        resultNumb = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            resultNumb[0] = max(resultNumb[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return resultNumb[0]
