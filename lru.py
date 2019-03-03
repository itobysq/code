from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: 'int'):
        self.idx_to_key = OrderedDict()
        self.capacity = capacity


    def get(self, key: 'int') -> 'int':
        if key in self.idx_to_key:
            val = self.idx_to_key.pop(key)
            self.idx_to_key[key] = val
            return val
        else:
            return -1

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.idx_to_key:
            val = self.idx_to_key.pop(key)
            self.idx_to_key[key] = value
        else:
            self.idx_to_key[key] = value
            if len(self.idx_to_key) > self.capacity:
                import pdb; pdb.set_trace()
                self.idx_to_key.popitem(last=False)

def first_case():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      # // returns 1
    cache.put(3, 3)   # // evicts key 2
    cache.get(2)      # // returns -1 (not found)
    cache.put(4, 4)   # // evicts key 1
    cache.get(1)      # // returns -1 (not found)
    cache.get(3)      # // returns 3
    cache.get(4)      # // returns 4

def second_case():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    cache.get(2)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      # // returns 1
    cache.put(3, 3)   # // evicts key 2
    cache.get(2)      # // returns -1 (not found)
    cache.put(4, 4)   # // evicts key 1
    cache.get(1)      # // returns -1 (not found)
    cache.get(3)      # // returns 3
    cache.get(4)      # // returns 4



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
