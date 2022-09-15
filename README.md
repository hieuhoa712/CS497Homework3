# CS497-Tech Interview-Homework3

# Hoa Fang

1. Because we are given sorted List, we only need to traverse the
list once while building the tree. The root of the list has to be the middle
node of the list. Everything on the left will be the left subtree and vice 
versa.

Basic Algorithm:

    listToBST(List)
        if headNode empty: return
        if headNode.next empty: return
        while both nextPtr and nextPtr.next:
            move the index toward
        break the node link
        construst left_subtree
        construct right_subtree

Time Complexity: O(n)

2. We are given a preorder and an inorder traversal. The first element in the
preorder traversal will be the root of our Binary Search Tree. Then, we look
at the root element in the inorder traversal. Any element to the left of root
number in the inorder traversal will belong the left subtree and vice versa.

Basic Algorithm:

    buildTree(List, List):
        for every element in each of the traversal
            index the number
        initialize stack
        for each value in preorder:
            if headNode empty:
                headNode is equal value of TreeNode
                append the headNode to the stack
            else
                node is the value of TreeNode
                if index value < index value inside the current stack
                    return node value
                else
                    for every lesser element
                    pop the element out of the stack

Time Complexity: O(nlog n)

3. Given that a node can only appear in the sequence at most once. We can use
DFS algorithm with recursive call to travers the branch first then lastly 
to the root. Then, we can put the maximum value of each branch upward to the
root.

Basic Algorithm:

    maxPathSum(TreeNode):
        default result is the root value
        dfs algorithm
            if root not found
                return
            left subtree search dfs
            right subtree search dfs
            recursive function setting max value for left subtree
            recursive function setting max value for right subtree
            result is = root + max value of left and right child

Time Complexity: O(n)

4. This is a typical problem for bfs algorithm. By using bfs, we only need to 
go through each row of the tree and insert the largest value into the output.

Basic Algorithm:

    largestValues(root):
        assign default value
        initialize root
        while at each row
            bfs to append max value into a queue

Time Complexity: O(n)

5. First, we use dfs algorithm to transverse the unbalanced tree which will
give us sorted List of all the elements. Then, we can construct balanced
BST using the sorted list we have gotten earlier.

Basic Algorithm:

    balanceBST(TreeNode):
        initialize value
        dfs to traverse the unbalanced tree 
            if node exist
                append the value in as queue data structure
            update the root value
        construct the bst
            if value is empty
                return none
            find the middle element of the sorted list
            construct the bst recursively

Time Complexity: O(nlog n)