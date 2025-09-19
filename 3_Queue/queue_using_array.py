# ===============================
# Array-Based Queue Implementation
# ===============================

class Queue:
    """
    Queue implementation using a fixed-size array.

    Theory:
        - A Queue is a linear data structure that follows FIFO (First In First Out).
        - Uses a contiguous memory array for storage.
        - Insertion (enqueue) happens at the rear, removal (dequeue) happens at the front.
        - Unlike linked lists, arrays have a fixed size and may require shifting elements after dequeues.

    Real-world Usage:
        - Job scheduling (print queue, CPU task scheduling)
        - Handling requests in servers
        - BFS traversal in graphs

    Complexity Overview:
        - Enqueue: O(1) (unless array is full)
        - Dequeue: O(n) (because elements are shifted)
        - Print Queue: O(n)
        - Space Complexity: O(MAX_SIZE) (fixed-size array)

    Problem with This Implementation:
        - Every dequeue operation shifts all elements to the left to fill the empty space.
        - This makes dequeue O(n) instead of O(1), which is inefficient for large queues.
        - Fixed-size array can become full even if there is free space at the front (after multiple dequeues).
        - To solve these problems, we implement a Circular Queue where both enqueue and dequeue are O(1)
          and we can fully utilize the array space.
    """
    def __init__(self, size):
        """
        Initialize an empty queue with a fixed size array.
        """
        self.MAX_SIZE = size
        self.arr = [None] * self.MAX_SIZE
        self.front = self.rear = -1  # -1 indicates empty queue

    # ===============================
    # QUEUE OPERATIONS
    # ===============================
    def enqueue(self, data):
        """
        Add a new element to the rear of the queue.

        Time Complexity:
            - O(1): Direct insertion at rear.
        Space Complexity:
            - O(1): Only uses a single array slot.

        Args:
            data (Any): The value to be inserted into the queue.

        Returns:
            None
        """
        if self.rear == self.MAX_SIZE - 1:
            print("Queue is full, no space for further enqueue")
            return

        if self.front == -1:  # First insertion
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.arr[self.rear] = data
        print(f"Element added to queue: {data}")

    def dequeue(self):
        """
        Remove the front element from the queue.

        Time Complexity:
            - O(n): All elements are shifted left after removing front.
        Space Complexity:
            - O(1): No extra space used.

        Returns:
            Any: The value of the dequeued element, or None if queue is empty.
        """
        if self.front == -1:  # Empty queue
            print("Queue is Empty, nothing to dequeue")
            return None

        popped_val = self.arr[self.front]
        print(f"Popped {popped_val} from the Queue")

        # Shift all elements one position to the left
        for idx in range(self.front + 1, self.rear + 1):
            self.arr[idx - 1] = self.arr[idx]
        self.rear -= 1

        # Queue becomes empty after this dequeue
        if self.front > self.rear:
            self.front = self.rear = -1

        return popped_val

    def print_queue(self):
        """
        Print all elements of the queue from front to rear in a visual format.

        Time Complexity:
            - O(n): Iterates through the elements between front and rear.
        Space Complexity:
            - O(1): No extra space used.

        Example Output:
            Front                           Rear
            |                               |
            v                               v
            10 -> 20 -> 30 -> 40 -> None
        """
        if self.front == -1:
            print("Queue is Empty, nothing to print")
            return

        # Print front and rear labels
        print(f"{'Front':<30}{'Rear'}")
        print(f"{'  |':<30}{'  |'}")
        print(f"{'  v':<30}{'  v'}")

        # Print queue elements from front to rear
        for i in range(self.front, self.rear + 1):
            print(self.arr[i], end="")
            if i != self.rear:
                print(" -> ", end="")
            else:
                print(" -> None", end="")
        print("\n")


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    queue = Queue(size = 10)

    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.print_queue()  # Visual queue print

    # Dequeue elements
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()