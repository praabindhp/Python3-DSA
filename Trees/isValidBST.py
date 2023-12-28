# Trees
# Write a function to determine if a binary tree is a valid binary search tree (BST).

# Input:
# A binary tree represented by its root node. Each node in the tree has a value, a left child reference, and a right child reference.

# Output:
# Return True if the binary tree is a valid BST; otherwise, return False.

# Constraints:

# Nodes have integer values.
# All values in the left subtree of a node should be less than the node's value.
# All values in the right subtree of a node should be greater than the node's value.
# There are no duplicate values in the tree.

# Example 1:
# #       2
# #      / \
# #     1   3
 
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
 
# # Expected Output: True (2 is the root, left child is 1, right child is 3)
# print(is_valid_bst(root))


# Example 2:
# #       2
# #      / \
# #     4   3
 
# root = TreeNode(2)
# root.left = TreeNode(4)
# root.right = TreeNode(3)
 
# # Expected Output: False (2 is the root, left child is 4 which is larger)
# print(is_valid_bst(root))

# Solution
def is_valid_bst(root):
    # Implement this function
    if (root.value > root.left.value) & (root.value < root.right.value):
        return True
    else:
        return False