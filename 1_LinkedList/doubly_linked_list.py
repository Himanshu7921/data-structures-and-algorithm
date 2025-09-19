class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        pass

    def insert_at_beginning(self, data):
        pass

    def insert_after_value(self, data):
        pass

    def delete_node(self, node):
        pass

    def delete_node_by_value(self, target):
        pass

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

if __name__ == "__main__":
    pass