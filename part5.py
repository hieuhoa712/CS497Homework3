class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeBalancing:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        val = []
        def dfs(node):
            if node:
                dfs(node.left)
                val.append(node.val)
                dfs(node.right)
        dfs(root)

        def bst(val):
            if not val:
                return None
            mid = len(val) // 2
            root = TreeNode(val[mid])
            root.left = bst(val[:mid])
            root.right = bst(val[mid + 1:])
            return root

        return bst(val)