class Node:
    """
    Node represents a single element in a Stack (implemented using a singly linked list).

    Theory:
        - A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle.
        - In this implementation, a singly linked list is used to store stack elements.
        - Each node contains:
            1. Data (value of the node).
            2. Next (reference to the next node in the list).
        - The "top" of the stack is represented by the last node of the linked list.

    Real-world Usage:
        - Function call management (call stack in programming languages).
        - Undo/Redo functionality in editors.
        - Expression evaluation (parentheses matching, infix to postfix conversion).

    Attributes:
        data (Any): The value stored in the node.
        next (Node): Reference to the next node in the stack.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Stack implementation using a singly linked list.

    Complexity Overview:
        - Push (insert at end): O(n)
        - Pop (remove from end): O(n)
        - Print stack: O(n)
        - Space Complexity: O(n) (each element requires an extra reference)

    Note:
        In this version, push and pop work at the end of the list, which requires traversal.
        If implemented at the head, push/pop would both be O(1).
    """
    def __init__(self):
        self.head = None

    # ===============================
    # INSERTION METHOD
    # ===============================
    def push(self, data):
        """
        Push a new element onto the stack.

        Time Complexity:
            - O(n): Traverses the entire linked list to append at the end.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            data (Any): The value to be pushed.

        Returns:
            Node: The newly inserted node.
        """
        if not self.head:  # Case 1: Empty stack
            new_node = Node(data)
            self.head = new_node
            return new_node

        # Case 2: Traverse to the end and insert
        temp = self.head
        while temp.next:
            temp = temp.next

        new_node = Node(data)
        temp.next = new_node
        return new_node

    # ===============================
    # DELETION METHOD
    # ===============================
    def pop(self):
        """
        Pop (remove and return) the top element from the stack.

        Time Complexity:
            - O(n): Traverses the list to reach the last node.
        Space Complexity:
            - O(1): No extra space required.

        Returns:
            Any: The value of the popped node.
            -1 if the stack is empty.

        Edge Cases:
            - If the stack is empty → prints a message and returns -1.
            - If only one element → head is set to None.
        """
        if not self.head:  # Case 1: Empty stack
            print("Stack is Empty, no data to pop. Stack Underflow")
            return -1

        temp = self.head

        if not self.head.next:  # Case 2: Single element
            popped_value = temp.data
            self.head = None
            print(f"Popped {popped_value} (last-element) from the stack")
            return popped_value

        # Case 3: Multiple elements → remove last
        while temp.next.next:
            temp = temp.next
        popped_value = temp.next.data
        temp.next = None
        print(f"Popped {popped_value} from the stack")
        return popped_value

    # ===============================
    # UTILITY METHOD
    # ===============================
    def print_stack(self):
        """
        Print all elements of the stack from bottom to top.

        Time Complexity:
            - O(n): Traverses the list once.
        Space Complexity:
            - O(1): No extra space used.

        Returns:
            -1 if the stack is empty, otherwise None.

        Example Output:
            Stack Elements: 10 20 30 40
            OR
            Stack is Empty, nothing to print
        """
        if self.head:
            temp = self.head
            print("Stack Elements: ", end=" ")
            while temp:
                print(f"{temp.data}", end=" ")
                temp = temp.next
            print()
        else:
            print("Stack is Empty, nothing to print")
            return -1


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    stack = Stack()

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    # Print stack
    stack.print_stack()  # Stack Elements: 10 20 30 40

    # Pop elements
    stack.pop()  # Popped 40
    stack.pop()  # Popped 30
    stack.pop()  # Popped 20
    stack.pop()  # Popped 10

    # Print after emptying
    stack.print_stack()  # Stack is Empty, nothing to print

    # Pop on empty
    stack.pop()  # Stack is Empty, no data to pop. Stack Underflow