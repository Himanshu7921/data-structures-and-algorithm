# ===============================
# Binary Search Tree Implementation
# ===============================

class TreeNode:
    """
    TreeNode represents a single node in a Binary Search Tree (BST).

    Theory:
        - A BST is a tree data structure where each node has at most two children.
        - Left subtree nodes contain values less than the node.
        - Right subtree nodes contain values greater than the node.
        - BST allows fast search, insertion, and deletion (O(log n) on average for balanced trees).

    Real-world Usage:
        - Used in databases and indexing for fast search operations.
        - Efficiently implements sets, maps, and priority queues.
        - Useful in memory management, symbol tables, and routing algorithms.

    Attributes:
        data (Any): Value stored in the node.
        left (TreeNode): Reference to the left child node.
        right (TreeNode): Reference to the right child node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # ===============================
    # INSERTION METHOD
    # ===============================
    def add_child(self, data):
        """
        Add a child node to the BST maintaining the BST property.

        Time Complexity:
            - O(h): where h is the height of the tree. O(log n) for balanced tree, O(n) for skewed.
        Space Complexity:
            - O(1) for iterative memory; recursion uses call stack.

        Args:
            data (Any): Value to be inserted.

        Returns:
            bool: True if inserted, False if duplicate.
        """
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
            return True
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)
            return True
        else:
            return False  # Duplicate value, not inserted

    # ===============================
    # TRAVERSAL METHODS
    # ===============================
    def inorder_traversal(self):
        """Inorder Traversal: Left → Root → Right. Prints nodes in sorted order."""
        if self.left:
            self.left.inorder_traversal()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        """Preorder Traversal: Root → Left → Right."""
        print(self.data, end=" ")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        """Postorder Traversal: Left → Right → Root."""
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.data, end=" ")

# ===============================
# BINARY TREE CLASS
# ===============================
class BinarySearchTree:
    """
    BinaryTree represents a Binary Search Tree and provides utilities for
    insertion, traversal, building from list, and visual printing.

    Complexity Overview:
        - Insertion/Search/Delete: O(h) where h = height of tree
        - Traversals: O(n)
        - Space Complexity: O(n) for n nodes (plus call stack for recursion)
    """
    def __init__(self, data):
        self.root = TreeNode(data)

    def add_child(self, data):
        """Add a value to the BST starting from root."""
        self.root.add_child(data)

    def inorder_traversal(self):
        """Print BST nodes using inorder traversal."""
        self.root.inorder_traversal()

    def preorder_traversal(self):
        """Print BST nodes using preorder traversal."""
        self.root.preorder_traversal()

    def postorder_traversal(self):
        """Print BST nodes using postorder traversal."""
        self.root.postorder_traversal()

    def build_tree(self, elements):
        """
        Build BST from a list of elements.

        Args:
            elements (list): List of values to insert. First element becomes root.
        """
        for i in range(1, len(elements)):
            self.root.add_child(elements[i])

    # ===============================
    # VISUAL PRINT METHOD
    # ===============================
    def print_tree(self, node=None, level=0):
        """
        Print the tree structure in the terminal visually.

        Args:
            node (TreeNode, optional): Node to start printing from. Defaults to root.
            level (int): Level of the current node (used for indentation).
        """
        if node is None:
            node = self.root
        
        if node is None:
            return
        
        print("    " * level + f" -{node.data}")
        
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    elements = [60, 70, 20, 40, 50, 60, 90, 15, 35, 100]
    binarytree = BinarySearchTree(elements[0])
    binarytree.build_tree(elements)
    binarytree.print_tree()
    
    print("Inorder Traversal: ", end=" ")
    binarytree.inorder_traversal()
    print()

    print("Preorder Traversal: ", end=" ")
    binarytree.preorder_traversal()
    print()

    print("Postorder Traversal: ", end=" ")
    binarytree.postorder_traversal()
    print()