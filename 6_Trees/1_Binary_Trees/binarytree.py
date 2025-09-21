# ===============================
# Binary Tree Implementation
# ===============================

class TreeNode:
    """
    TreeNode represents a single node in a Binary Tree.

    Theory:
        - A Binary Tree is a hierarchical data structure in which each node has at most 2 children:
            1. Left Child
            2. Right Child
        - It is not necessarily sorted like a Binary Search Tree (BST).
        - Useful for representing hierarchical relationships such as:
            - Organization structures
            - File systems
            - Expression trees

    Attributes:
        data (Any): The value stored in the node.
        left (TreeNode): Reference to the left child.
        right (TreeNode): Reference to the right child.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree implementation with insertion, deletion (with replacement), 
    and traversal (printing) operations.

    Complexity Overview:
        - Insertion: O(1) (places node in first available child position).
        - Deletion:
            - Leaf node: O(1)
            - Node with children: O(h), where h is the height of the subtree 
              (to find and reattach children).
        - Traversal/Printing: O(n)
        - Space Complexity: O(n), as each node stores 2 references (left, right).
    """
    def __init__(self, data):
        # Initialize tree with root node
        self.root = TreeNode(data)
    
    # ===============================
    # INSERTION METHOD
    # ===============================
    def add_child(self, parent_node, child_data):
        """
        Add a child node under the given parent node.
        - If right child is free, it is placed there.
        - Otherwise, it is placed as the left child.

        Time Complexity:
            - O(1): Direct reference assignment.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            parent_node (TreeNode): Parent under which child is added.
            child_data (Any): Value to be inserted.

        Returns:
            TreeNode: Newly created child node.
        """
        child_node = TreeNode(child_data)

        if parent_node.right is None:
            parent_node.right = child_node
        elif parent_node.left is None:
            parent_node.left = child_node

        return child_node
    
    # ===============================
    # TRAVERSAL METHOD
    # ===============================
    def print_tree(self, node=None, level=0):
        """
        Print the tree structure starting from the given node 
        (defaults to root). Indentation represents levels.

        Time Complexity:
            - O(n): Visits every node once.
        Space Complexity:
            - O(h): Recursive call stack, where h is the tree height.
        """
        if node is None:
            node = self.root
        if node is None:
            return

        # Print current node with indentation based on depth
        print("   " * level + " -" + str(node.data))

        # Recursive printing of left and right children
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)
    
    # ===============================
    # DELETION METHODS
    # ===============================
    def remove_full_branch(self, parent_node, child_node):
        """
        Remove an entire subtree (branch) rooted at child_node.

        Time Complexity:
            - O(1): Just nullifies reference.
        Space Complexity:
            - O(1).

        Args:
            parent_node (TreeNode): Parent of the node to delete.
            child_node (TreeNode): The subtree root to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if parent_node.left == child_node:
            parent_node.left = None
            return True
        elif parent_node.right == child_node:
            parent_node.right = None
            return True
        else:
            return False
    
    def remove_node_and_replace(self, parent_node, child_node):
        """
        Remove a node and replace it with one of its children, if any.

        Rules:
            - If both children exist: Left child becomes replacement. 
              The right child is reattached to the rightmost node of left subtree.
            - If only one child exists: That child replaces the node.
            - If leaf node: Simply removed.

        Time Complexity:
            - O(h): Traverses down to rightmost node of left subtree in worst case.
        Space Complexity:
            - O(1).

        Args:
            parent_node (TreeNode): Parent of the node to remove.
            child_node (TreeNode): Node being removed.

        Returns:
            bool: True if removal and replacement succeed, False otherwise.
        """
        # If child_node is parent's left
        if parent_node.left == child_node:
            if child_node.left and child_node.right:
                # Case: Both children exist
                replacement = child_node.left
                # Find rightmost node in left subtree
                current = replacement
                while current.right:
                    current = current.right
                current.right = child_node.right
                parent_node.left = replacement

            elif child_node.left:
                # Case: Only left child
                parent_node.left = child_node.left
            elif child_node.right:
                # Case: Only right child
                parent_node.left = child_node.right
            else:
                # Case: Leaf node
                parent_node.left = None
            return True

        # If child_node is parent's right
        elif parent_node.right == child_node:
            if child_node.left and child_node.right:
                replacement = child_node.left
                current = replacement
                while current.right:
                    current = current.right
                current.right = child_node.right
                parent_node.right = replacement

            elif child_node.left:
                parent_node.right = child_node.left
            elif child_node.right:
                parent_node.right = child_node.right
            else:
                parent_node.right = None
            return True

        return False


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    tree = BinaryTree(10)

    # Insert children under root
    node_20 = tree.add_child(tree.root, 20)
    node_30 = tree.add_child(tree.root, 30)
    
    # Add grandchildren
    node_40 = tree.add_child(node_20, 40)
    node_50 = tree.add_child(node_20, 50)
    node_60 = tree.add_child(node_30, 60)
    node_70 = tree.add_child(node_30, 70)

    node_100 = tree.add_child(node_60, 100)
    node_110 = tree.add_child(node_60, 110)
    node_80 = tree.add_child(node_70, 80)
    node_90 = tree.add_child(node_70, 90)

    node_140 = tree.add_child(node_40, 140)
    node_150 = tree.add_child(node_40, 150)
    node_120 = tree.add_child(node_50, 120)
    node_130 = tree.add_child(node_50, 130)

    # ----------------------------
    # Step 1: Original tree
    # ----------------------------
    print("Original Tree:")
    tree.print_tree()
    print()

    # ----------------------------
    # Step 2: Remove node 70
    # ----------------------------
    tree.remove_node_and_replace(node_30, node_70)
    print("After Removing 70:")
    tree.print_tree()
    print()

    # ----------------------------
    # Step 3: Remove node 30 (which now has one child 60)
    # ----------------------------
    tree.remove_node_and_replace(tree.root, node_30)
    print("After Removing 30:")
    tree.print_tree()
    print()
