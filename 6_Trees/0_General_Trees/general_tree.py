# ===============================
# General Tree Implementation
# ===============================

class TreeNode:
    """
    TreeNode represents a single node in a General Tree.

    Theory:
        - A General Tree is a hierarchical data structure where each node can have
          zero or more children.
        - Unlike binary trees, there is no restriction on the number of children.
        - Each node stores:
            1. data (value of the node)
            2. children (list of child nodes)

    Real-world Usage:
        - Organizational charts, file systems, or category hierarchies.
        - Representing XML/JSON data structures.
        - Modeling hierarchical relationships.

    Attributes:
        data (Any): The value stored in the node.
        children (list[TreeNode]): List of child nodes.
    """
    def __init__(self, data):
        self.data = data
        self.children = []


class GeneralTree:
    """
    General Tree implementation with methods to add children and print hierarchy.

    Complexity Overview:
        - Adding a child: O(1) per insertion
        - Printing the tree: O(n), where n is total number of nodes
        - Space Complexity: O(n) (for storing nodes and children lists)
    """
    def __init__(self, data):
        """
        Initialize a General Tree with a root node.

        Args:
            data (Any): The value of the root node.
        """
        self.root = TreeNode(data)

    # ===============================
    # ADD CHILD METHOD
    # ===============================
    def add_child(self, parent_node, child_data):
        """
        Add a new child node to a given parent node.

        Time Complexity:
            - O(1): Appending a new child to the parent's children list.
        Space Complexity:
            - O(1): Only the new child node is created.

        Args:
            parent_node (TreeNode): Node to which the child will be added.
            child_data (Any): Value of the new child node.

        Returns:
            TreeNode: The newly created child node.
        """
        child_node = TreeNode(child_data)
        parent_node.children.append(child_node)
        return child_node

    # ===============================
    # PRINT TREE METHOD
    # ===============================
    def print_tree(self, node=None, level=0):
        """
        Print the General Tree in a hierarchical view.

        Time Complexity:
            - O(n): Traverses every node in the tree.
        Space Complexity:
            - O(h): Recursion stack space, where h is height of the tree.

        Args:
            node (TreeNode, optional): Node to start printing from. Defaults to root.
            level (int, optional): Current tree level for indentation. Defaults to 0.

        Example Output:
            -Company
                -IT
                    -Aarav
                    -Diya
                -HR
                    -Karan
                    -Meera
        """
        if node is None:
            node = self.root
        
        print("    " * level + f" -{node.data}")
        for child in node.children:
            self.print_tree(child, level=level+1)


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    tree = GeneralTree("Company")

    # Add departments
    it_department = tree.add_child(tree.root, "IT")
    hr_department = tree.add_child(tree.root, "HR")
    finance_department = tree.add_child(tree.root, "Finance")
    tech_department = tree.add_child(tree.root, "Tech")
    ai_department = tree.add_child(tree.root, "AI")
    rnd_department = tree.add_child(tree.root, "Research and Development")

    # Add employees to IT
    tree.add_child(it_department, "Aarav")
    tree.add_child(it_department, "Diya")

    # Add employees to HR
    tree.add_child(hr_department, "Karan")
    tree.add_child(hr_department, "Meera")

    # Add employees to Finance
    tree.add_child(finance_department, "Rohan")
    tree.add_child(finance_department, "Sneha")

    # Add employees to Tech
    tree.add_child(tech_department, "Soumya")
    tree.add_child(tech_department, "Anaya")

    # Add employees to AI
    tree.add_child(ai_department, "Vivaan")
    tree.add_child(ai_department, "Isha")

    # Add employees to R&D
    tree.add_child(rnd_department, "Arjun")
    tree.add_child(rnd_department, "Priya")

    # Print the tree hierarchy
    tree.print_tree()