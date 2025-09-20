class HashSet:
    def __init__(self, size):
        self.MAX_SIZE = size
        self.arr = [None] * self.MAX_SIZE

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX_SIZE

    def append(self, val):
        hash = self.get_hash(val)
        found = False
        if self.arr[hash] is not None:
            found = True
        if not found:
            self.arr[hash] = val 

    def print_hashset(self):
        print("{", end="")
        for idx, element in enumerate(self.arr):
            if element is not None:
                print(element, end=", ")
        print("}")


if __name__ == "__main__":
    hashset = HashSet(10)

    # Add elements with intended collision
    hashset.append("abc")  # hash("abc") % 10
    hashset.append("cab")  # hash("cab") % 10 → same as "abc", collision happens
    hashset.append("xyz")
    hashset.append("yzx")  # another collision with "xyz"

    hashset.print_hashset()
    
    print(f"Hash of 'abc' = {hashset.get_hash('abc')}")
    print(f"Hash of 'cab' = {hashset.get_hash('cab')}")
    print(f"Hash of 'xyz' = {hashset.get_hash('xyz')}")
    print(f"Hash of 'yzx' = {hashset.get_hash('yzx')}")