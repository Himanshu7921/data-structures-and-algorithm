# ===============================
# Linked List Implementation
# ===============================

class Node:
    """
    Node represents a single element in a Linked List.

    Theory:
        - A Linked List is a linear data structure where elements (nodes) are stored 
          at non-contiguous memory locations.
        - Each node contains:
            1. Data (value of the node).
            2. Next (reference to the next node in the list).
        - Unlike arrays, linked lists do not require continuous memory, 
          and insertion/deletion is efficient at arbitrary positions.

    Real-world Usage:
        - Implementing dynamic data structures like stacks, queues, and adjacency lists.
        - Useful when frequent insertions/deletions are required without shifting elements.
        - Used in memory management and file systems.

    Attributes:
        data (Any): The value stored in the node.
        next (Node): Reference to the next node in the Linked List.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly Linked List implementation with insertion, deletion, and traversal operations.

    Complexity Overview:
        - Insertion at beginning: O(1)
        - Insertion at end: O(n)
        - Insertion after node/value: O(n)
        - Deletion by node/value: O(n)
        - Traversal/Print: O(n)
        - Space Complexity: O(n) (since each node takes extra memory for a reference)
    """
    def __init__(self):
        self.head = None

    # ===============================
    # INSERTION METHODS
    # ===============================
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the Linked List.

        Time Complexity:
            - O(n): Traverses the entire list to reach the last node.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            data (Any): The value to be inserted.

        Returns:
            Node: The newly inserted node.
        """
        new_node = Node(data)

        if not self.head:  # Case 1: Empty list
            self.head = new_node
            return new_node

        # Case 2: Traverse to the end
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return new_node

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the Linked List.

        Time Complexity:
            - O(1): No traversal required, direct insertion at head.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            data (Any): The value to be inserted.

        Returns:
            Node: The newly inserted node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def insert_after(self, prev_node, data):
        """
        Insert a new node after a given node.

        Time Complexity:
            - O(1): Insertion happens in constant time if prev_node is given.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            prev_node (Node): Node after which new node will be inserted.
            data (Any): The value to be inserted.

        Returns:
            Node: The newly inserted node, or None if prev_node is invalid.
        """
        if not prev_node:
            print("Previous node must be in the Linked List.")
            return None

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return new_node

    def insert_after_value(self, target, data):
        """
        Insert a new node after the first occurrence of a target value.

        Time Complexity:
            - O(n): Traverses the list until target is found.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            target (Any): The value after which insertion happens.
            data (Any): The value to be inserted.

        Returns:
            Node: The newly inserted node, or None if target not found.
        """
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return new_node
            temp = temp.next

        print(f"Value {target} not found in the list.")
        return None

    # ===============================
    # DELETION METHODS
    # ===============================
    def delete_node(self, node):
        """
        Delete a given node from the Linked List.

        Time Complexity:
            - O(n): Traverses list to find the node.
        Space Complexity:
            - O(1): No extra space used.

        Args:
            node (Node): The node to be deleted.

        Returns:
            Any: Data of the deleted node, or None if node not found.
        """
        if not self.head:
            return None

        # Case 1: Deleting head node
        if node == self.head:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data

        # Case 2: Delete other node
        temp = self.head
        while temp.next != node and temp.next is not None:
            temp = temp.next

        if not temp.next:  # Node not found
            return None

        deleted_node_data = node.data
        temp.next = node.next
        return deleted_node_data

    def delete_node_by_value(self, target):
        """
        Delete the first node containing the target value.

        Time Complexity:
            - O(n): Traverses the list until the target is found.
        Space Complexity:
            - O(1): No extra space used.

        Args:
            target (Any): Value of the node to be deleted.

        Returns:
            Any: Data of the deleted node, or None if value not found.
        """
        if not self.head:
            return None

        # Case 1: Delete head
        if self.head.data == target:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data

        # Case 2: Delete other nodes
        temp = self.head
        while temp.next and temp.next.data != target:
            temp = temp.next

        if not temp.next:  # Value not found
            return None

        deleted_node_data = temp.next.data
        temp.next = temp.next.next
        return deleted_node_data

    # ===============================
    # UTILITY METHODS
    # ===============================
    def print_linked_list(self):
        """
        Print the Linked List in readable format.

        Time Complexity:
            - O(n): Traverses entire list.
        Space Complexity:
            - O(1): No extra space.

        Example Output:
            10 --> 20 --> 30 --> None
        """
        temp = self.head
        while temp:
            if temp.next is None:
                print(f"{temp.data} --> None", end=" ")
            else:
                print(f"{temp.data} --> ", end=" ")
            temp = temp.next
        print()


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    list_1 = LinkedList()

    # Insert at end
    n1 = list_1.insert_at_end(10)  # head
    n2 = list_1.insert_at_end(20)
    n3 = list_1.insert_at_end(30)
    n4 = list_1.insert_at_end(40)
    list_1.print_linked_list()  # 10 --> 20 --> 30 --> 40 --> None

    # Insert at beginning
    n5 = list_1.insert_at_beginning(0)
    list_1.print_linked_list()  # 0 --> 10 --> 20 --> 30 --> 40 --> None

    # Insert after node
    n6 = list_1.insert_after(n5, 1000)
    list_1.print_linked_list()  # 0 --> 1000 --> 10 --> 20 --> 30 --> 40 --> None

    # Insert after value
    n7 = list_1.insert_after_value(20, 9000)
    list_1.print_linked_list()  # 0 --> 1000 --> 10 --> 20 --> 9000 --> 30 --> 40 --> None

    # Delete by node reference
    list_1.delete_node(n7)
    list_1.delete_node(n6)
    list_1.print_linked_list()  # 0 --> 10 --> 20 --> 30 --> 40 --> None

    # Delete by value
    list_1.delete_node_by_value(30)
    list_1.print_linked_list()  # 0 --> 10 --> 20 --> 40 --> None