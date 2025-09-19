# ===============================
# Linear Linked List Queue Implementation
# ===============================

class Node:
    """
    Node represents a single element in a Queue implemented using a singly Linked List.

    Theory:
        - A Queue is a linear data structure that follows FIFO (First In First Out).
        - Each node contains:
            1. Data (value of the node)
            2. Next (reference to the next node in the Queue)
        - Unlike arrays, linked lists allow dynamic memory allocation, 
          making insertion and deletion efficient without shifting elements.

    Real-world Usage:
        - Job scheduling (print queue, CPU task scheduling)
        - Handling requests in servers
        - BFS traversal in graphs

    Attributes:
        data (Any): The value stored in the node.
        next (Node): Reference to the next node in the Queue.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinearLinkedListQueue:
    """
    Queue implementation using a singly linked list.

    Theory:
        - Uses two pointers: front (for removal) and rear (for insertion)
        - Enqueue adds at rear; Dequeue removes from front
        - FIFO structure is maintained

    Complexity Overview:
        - Enqueue: O(1) (insert at rear)
        - Dequeue: O(1) (remove from front)
        - Print Queue: O(n)
        - Space Complexity: O(n) (one node object per element)
    """
    def __init__(self):
        self.front = self.rear = None  # Initialize empty queue

    # ===============================
    # QUEUE OPERATIONS
    # ===============================
    def enqueue(self, data):
        """
        Insert a new element at the rear of the Queue.

        Time Complexity:
            - O(1): Only pointer adjustment required.
        Space Complexity:
            - O(1): Only a new node is created.

        Args:
            data (Any): Value to be added to the Queue.

        Returns:
            None

        Example:
            queue.enqueue(10)
        """
        new_node = Node(data)
        if not self.rear and not self.front:  # Queue empty
            self.rear = self.front = new_node
            print(f"Inserted 1st Element into the Queue: {data}")
        else:
            self.rear.next = new_node
            self.rear = new_node
            print(f"Inserted new Element into the Queue: {data}")

    def dequeue(self):
        """
        Remove the front element from the Queue.

        Time Complexity:
            - O(1): Directly removes the front node.
        Space Complexity:
            - O(1): No extra space used.

        Returns:
            Any: Value of the dequeued node, or -1 if Queue is empty.

        Example:
            queue.dequeue()  # Pops front element
        """
        if not self.front:  # Queue empty
            print("Queue is Empty, nothing to dequeue")
            return -1

        popped_val = self.front.data
        self.front = self.front.next
        print(f"Popped {popped_val} from the Queue")
        return popped_val

        

    def print_queue(self):
        """
        Print all elements of the Queue from front to rear in a visual format.

        Time Complexity:
            - O(n): Traverses the list once.
        Space Complexity:
            - O(1): No extra space used.

        Example Output:
            Front                           Rear
            |                               |
            v                               v
            10 -> 20 -> 30 -> 40 -> None
        """
        if not self.front:
            print("Queue is Empty, nothing to print")
            return -1

        # Print front and rear pointers
        print(f"{'Front':<30}{'Rear'}")
        print(f"{'  |':<30}{'  |'}")
        print(f"{'  v':<30}{'  v'}")

        # Print the queue elements
        temp = self.front
        while temp:
            print(f"{temp.data}", end="")
            if temp.next:
                print(" -> ", end="")
            else:
                print(" -> None", end="")
            temp = temp.next
        print("\n")



# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    queue = LinearLinkedListQueue()
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.print_queue()  # Queue Elements: 40 30 20 10

    # Dequeue elements
    queue.dequeue()  # Popped 10 from the Queue
    queue.dequeue()  # Popped 20 from the Queue
    queue.print_queue()
    queue.dequeue()  # Popped 30 from the Queue
    queue.dequeue()  # Popped 40 from the Queue
    queue.print_queue()  # Queue is Empty, nothing to print
    queue.dequeue()  # Queue is Empty, nothing to dequeue

    # Print empty queue
    queue.print_queue()  # Queue is Empty, nothing to print