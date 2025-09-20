# ===============================
# Hash Set Implementation
# ===============================

class HashSet:
    """
    HashSet implementation using Separate Chaining for collision handling.

    Theory:
        - A HashSet is a data structure that stores unique values.
        - Values are hashed to determine their position in an array.
        - Collisions (two values mapping to the same index) are handled using lists
          (separate chaining).
        - Duplicate values are not allowed.

    Real-world Usage:
        - Removing duplicates from data.
        - Efficient membership checks (O(1) average time).
        - Fast lookups for unique items in collections.

    Complexity Overview:
        - Average Case:
            Insert: O(1)
            Search: O(1)
        - Worst Case (many collisions in one bucket):
            Insert: O(n)
            Search: O(n)
        - Space Complexity: O(n), where n is the number of values.
    """

    def __init__(self, size):
        """
        Initialize the HashSet with a given number of buckets.

        Args:
            size (int): Number of buckets in the HashSet.
        """
        self.MAX_SIZE = size
        self.arr = [[] for _ in range(self.MAX_SIZE)]  # Each bucket is a list for collisions

    def get_hash(self, key):
        """
        Compute the hash value (bucket index) for a given key.

        Time Complexity:
            - O(k), where k is the length of the key (sum of ASCII values).
        Space Complexity:
            - O(1)

        Args:
            key (str): The value to be hashed.

        Returns:
            int: Index of the bucket in the range [0, MAX_SIZE-1].
        """
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX_SIZE

    def append(self, val):
        """
        Add a value to the HashSet if it does not already exist.

        Time Complexity:
            - Average Case: O(1)
            - Worst Case (bucket has many collisions): O(n)
        Space Complexity:
            - O(1) for the value itself, O(n) for the bucket in worst case.

        Args:
            val (str): The value to add to the set.
        """
        hash_val = self.get_hash(val)
        found = False
        for element in self.arr[hash_val]:
            if element == val:  # Check for duplicates
                found = True
                break
        if not found:
            self.arr[hash_val].append(val)  # Insert value in bucket

    def print_hashset(self):
        """
        Print all elements in the HashSet in a readable format.

        Time Complexity:
            - O(n + m), where n is the number of buckets and m is the total number of elements.
        Space Complexity:
            - O(1)

        Example Output:
            {abc, cab, xyz, yzx}
        """
        print("{", end="")
        elements = []
        for bucket in self.arr:
            for element in bucket:
                if element is not None:
                    elements.append(element)
        print(", ".join(elements), end="")
        print("}")
    
    # ===============================
    # DELETION METHOD
    # ===============================
    def remove(self, val):
        """
        Delete a value from the HashSet if it exists.

        Time Complexity:
            - Average Case: O(1)
            - Worst Case: O(n) if bucket is large due to collisions.
        Space Complexity:
            - O(1)

        Args:
            val (str): The value to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.

        Example:
            del hashset["abc"]
        """
        hash_val = self.get_hash(val)
        bucket = self.arr[hash_val]

        for idx, element in enumerate(bucket):
            if element == val:
                del bucket[idx]
                return True
        return False


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    hashset = HashSet(10)

    # Add elements with intended collisions
    hashset.append("abc")  # hash("abc") % 10
    hashset.append("cab")  # hash("cab") % 10 → same as "abc", collision handled
    hashset.append("xyz")
    hashset.append("yzx")  # collision with "xyz", still handled

    # Print HashSet
    print("Initial HashSet:")
    hashset.print_hashset()  # {abc, cab, xyz, yzx}

    # Print hash values of inserted elements
    print(f"Hash of 'abc' = {hashset.get_hash('abc')}")
    print(f"Hash of 'cab' = {hashset.get_hash('cab')}")
    print(f"Hash of 'xyz' = {hashset.get_hash('xyz')}")
    print(f"Hash of 'yzx' = {hashset.get_hash('yzx')}")

    # Delete an element
    print("\nDeleting 'cab'...")
    result = hashset.remove("cab")
    print("Deleted successfully!" if result else "Value not found.")

    # Print HashSet after deletion
    print("HashSet after deletion:")
    hashset.print_hashset()  # {abc, xyz, yzx}