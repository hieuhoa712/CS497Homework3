class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class makeBST:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i

        stack = []
        headNode = None
        for val in preorder:
            if not headNode:
                headNode = TreeNode(val)
                stack.append(headNode)
            else:
                node = TreeNode(val)
                if index[val] < index[stack[-1].val]:
                    stack[-1].left = node
                else:
                    while stack and index[stack[-1].val] < index[val]:
                        numb = stack.pop()
                    numb.right = node
                stack.append(node)
        return headNode
