# ===============================
# Circular Queue Implementation
# ===============================

class CircularQueue:
    """
    Circular Queue implementation using a fixed-size array.

    Theory:
        - A Queue is a linear data structure that follows FIFO (First In, First Out).
        - A Circular Queue is a variation where the last position is connected back
          to the first position, forming a circle.
        - This avoids the shifting overhead of a linear queue and reuses empty slots.
        
    Key Points:
        - Front: Points to the first element of the queue.
        - Rear: Points to the last element of the queue.
        - Queue Full condition: (rear + 1) % MAX_SIZE == front
        - Queue Empty condition: front == -1

    Real-world Usage:
        - CPU scheduling (Round Robin).
        - Memory management (buffering, resource allocation).
        - Handling real-time data streams (network packets, IO devices).

    Complexity Overview:
        - Enqueue: O(1)
        - Dequeue: O(1)
        - Print/Traversal: O(n)
        - Space Complexity: O(n) (fixed-size array of size MAX_SIZE)
    """

    def __init__(self, size):
        """
        Initialize the Circular Queue.

        Args:
            size (int): Maximum capacity of the queue.
        """
        self.MAX_SIZE = size
        self.arr = [None] * self.MAX_SIZE
        self.front = self.rear = -1  # -1 indicates empty queue

    # ===============================
    # ENQUEUE METHOD
    # ===============================
    def enqueue(self, data):
        """
        Insert an element into the Circular Queue.

        Time Complexity:
            - O(1): Uses modulo to directly calculate rear position.
        Space Complexity:
            - O(1): No extra space needed.

        Args:
            data (Any): The element to be inserted.
        """
        if (self.rear + 1) % self.MAX_SIZE == self.front:  # Queue is full
            print("Queue is Full, can't insert new elements")
            return

        if self.front == -1:  # First element being added
            self.front = 0

        self.rear = (self.rear + 1) % self.MAX_SIZE
        self.arr[self.rear] = data
        print(f"Enqueued {data} to the queue.")

    # ===============================
    # DEQUEUE METHOD
    # ===============================
    def dequeue(self):
        """
        Remove an element from the Circular Queue.

        Time Complexity:
            - O(1): Directly removes from front position.
        Space Complexity:
            - O(1): No extra space used.

        Returns:
            Any: The dequeued value, or None if queue is empty.
        """
        if self.front == -1:  # Empty queue
            print("Queue is Empty, can't dequeue further more")
            return None

        popped_val = self.arr[self.front]

        # Queue becomes empty after removing last element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX_SIZE

        print(f"Dequeued {popped_val} from the queue.")
        return popped_val

    # ===============================
    # PRINT METHOD
    # ===============================
    def print_queue(self):
        """
        Print all elements of the Circular Queue from front to rear.

        Time Complexity:
            - O(n): Traverses all elements currently in the queue.
        Space Complexity:
            - O(1): No extra space used.

        Example Output:
            Queue Elements: 
            10 20 30 40
        """
        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Queue Elements: ", end = "")
        i = self.front
        while True:
            print(self.arr[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.MAX_SIZE
        print()


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    circular_queue = CircularQueue(5)

    # Enqueue operations
    circular_queue.enqueue(10)
    circular_queue.enqueue(20)
    circular_queue.enqueue(30)
    circular_queue.enqueue(40)
    circular_queue.print_queue()  # 10 20 30 40

    # Dequeue operations
    circular_queue.dequeue()
    circular_queue.dequeue()

    # Reusing slots after dequeue
    circular_queue.enqueue(50)
    circular_queue.enqueue(60)
    circular_queue.enqueue(70)
    circular_queue.print_queue()  # 30 40 50 60 70
    circular_queue.dequeue()
    circular_queue.enqueue(80)
    circular_queue.print_queue()  # 40 50 60 70 80