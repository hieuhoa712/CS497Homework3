class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
