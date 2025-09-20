# ===============================
# Hash Map Implementation
# ===============================

class HashMap:
    """
    HashMap implementation using Separate Chaining for collision handling.

    Theory:
        - A HashMap (or dictionary) is a data structure that stores key-value pairs.
        - Keys are converted into array indices using a hash function.
        - Collisions (two keys mapping to the same index) are handled using lists 
          (separate chaining).
        - Provides efficient lookups, insertions, and deletions.

    Real-world Usage:
        - Storing user profiles with unique IDs as keys.
        - Database indexing for fast search and retrieval.
        - Caching frequently used computations or API responses.

    Complexity Overview:
        - Average Case:
            Insert: O(1)
            Search: O(1)
            Delete: O(1)
        - Worst Case (when many collisions occur):
            Insert: O(n)
            Search: O(n)
            Delete: O(n)
        - Space Complexity: O(n), where n is the number of key-value pairs.
    """

    def __init__(self, size):
        """
        Initialize the HashMap with a given size.

        Args:
            size (int): The maximum size of the HashMap (number of buckets).
        """
        self.MAX_SIZE = size
        self.arr = [[] for _ in range(self.MAX_SIZE)]  # Each bucket is a list

    def get_hash(self, key):
        """
        Compute the hash value (bucket index) for a given key.

        Time Complexity:
            - O(k), where k is the length of the key (summing ASCII values).
        Space Complexity:
            - O(1)

        Args:
            key (str): The key to be hashed.

        Returns:
            int: The hash index within the range [0, MAX_SIZE-1].
        """
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX_SIZE

    def __setitem__(self, key, val):
        """
        Insert or update a key-value pair in the HashMap.

        Time Complexity:
            - Average Case: O(1)
            - Worst Case (collision-heavy): O(n) for traversing the bucket.
        Space Complexity:
            - O(1)

        Args:
            key (str): The key to insert.
            val (Any): The value associated with the key.
        """
        hash = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                found = True
                self.arr[hash][idx] = (key, val)  # Update existing key
                break
        if not found:
            self.arr[hash].append((key, val))  # Insert new key-value pair

    def __getitem__(self, key):
        """
        Retrieve the value associated with a given key.

        Time Complexity:
            - Average Case: O(1)
            - Worst Case: O(n), traversing bucket list in case of collisions.
        Space Complexity:
            - O(1)

        Args:
            key (str): The key to search for.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found in the HashMap.
        """
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
        raise KeyError(f"key '{key}' not found")


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    hashmap = HashMap(10)
    hashmap["title"] = "Vagabond"
    hashmap["author"] = "Takehiko Inoue"
    hashmap["year"] = 1998

    # Force a collision with "title"
    hashmap["paper"] = "Weekly Morning Magazine"

    print("Manga Title:", hashmap["title"])
    print("Manga Author:", hashmap["author"])
    print("Published Year:", hashmap["year"])
    print("Serialized In:", hashmap["paper"])  # Same bucket as "title"

    print(f"Hash of 'title' = {hashmap.get_hash('title')}")
    print(f"Hash of 'author' = {hashmap.get_hash('author')}")
    print(f"Hash of 'year' = {hashmap.get_hash('year')}")
    print(f"Hash of 'paper' = {hashmap.get_hash('paper')}")

    print("\nInternal HashMap Buckets:")
    print(hashmap.arr)