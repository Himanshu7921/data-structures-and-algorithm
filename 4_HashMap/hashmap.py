# ===============================
# Hash Map Implementation (No Collision Handling)
# ===============================

class HashMap:
    """
    HashMap implementation without collision handling.

    Theory:
        - A HashMap stores key-value pairs by converting keys into array indices.
        - In this simplified version, collisions are ignored.
        - If two keys hash to the same index, the later one overwrites the previous value.

    Real-world Usage:
        - Educational purpose (to learn hashing basics).
        - Situations where we know in advance that collisions won't occur.

    Complexity Overview:
        - Insert: O(1)
        - Search: O(1)
        - Delete: O(1)
        - Space Complexity: O(n), where n is the number of buckets.
    """

    def __init__(self, size):
        """
        Initialize the HashMap with a given size.

        Args:
            size (int): The maximum size of the HashMap (number of buckets).
        """
        self.MAX_SIZE = size
        self.arr = [None] * self.MAX_SIZE  # Each bucket holds one key-value pair

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

        Note: Collisions are not handled. 
        If a collision occurs, the value at that index will be overwritten.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        hash = self.get_hash(key)
        self.arr[hash] = val  # Direct assignment

    def __getitem__(self, key):
        """
        Retrieve the value associated with a given key.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            Any: The value associated with the key.
        """
        hash = self.get_hash(key)
        val = self.arr[hash]
        if val is None:
            raise KeyError(f"key '{key}' not found")
        return val


# ===============================
# DEMO USAGE
# ===============================
if __name__ == "__main__":
    hashmap = HashMap(10)
    hashmap["title"] = "Vagabond"
    hashmap["author"] = "Takehiko Inoue"
    hashmap["year"] = 1998

    print("Manga Title:", hashmap["title"])
    print("Manga Author:", hashmap["author"])
    print("Published Year:", hashmap["year"])

    print(f"Hash of 'title' = {hashmap.get_hash('title')}")
    print(f"Hash of 'author' = {hashmap.get_hash('author')}")
    print(f"Hash of 'year' = {hashmap.get_hash('year')}")

    print("\nInternal HashMap Buckets:")
    print(hashmap.arr)