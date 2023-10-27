from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to represent it as the most recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            # If the key already exists, update its value and move it to the end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is full, remove the least recently used item (the first item)
                self.cache.popitem(last=False)
            # Add the new key-value pair to the cache
            self.cache[key] = value



# Example usage of the LRU cache
cache = LRUCache(3)

cache.put("key1", "value1")
cache.put("key2", "value2")
cache.put("key3", "value3")

print("Key1:", cache.get("key1"))  # Should return "value1"
print("Key2:", cache.get("key2"))  # Should return "value2"
print("Key3:", cache.get("key3"))  # Should return "value3"

# Adding a new key-value pair should trigger eviction
cache.put("key4", "value4")

print("Key1:", cache.get("key1"))  # Should return None (evicted)
