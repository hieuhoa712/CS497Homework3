class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.val = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class List2Tree:
    def listToBST(self, headNode: ListNode) -> TreeNode:

        if not headNode:
            return None
        if not headNode.next:
            return TreeNode(headNode.val)

        slowPtr = fastPtr = headNode
        preNode = None
        while fastPtr and fastPtr.next:
            preNode = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        preNode.next = None

        root = TreeNode(slowPtr.val)
        root.left = self.listToBST(headNode)
        root.right = self.listToBST(slowPtr.next)

        return root