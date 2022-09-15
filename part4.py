class TreeLargest:
    def largestValues(self, root):
        maxValue = []
        BSTrow = [root]
        while any(BSTrow):
            maxValue.append(max(node.val for node in BSTrow))
            BSTrow = [childNode for TreeNode in BSTrow for childNode in (TreeNode.left, TreeNode.right) if childNode]
        return maxValue  