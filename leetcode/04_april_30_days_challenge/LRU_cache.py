# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            key = list(self.dic)[0]
            self.dic.pop(key)


cache = LRUCache(2)

# cache.put(2, 1)
# cache.put(1, 1)
#
# cache.put(2, 3)
# cache.put(4, 1)
# print(cache.get(1))  # -1)
# print(cache.get(2))  # 3

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4

print('done')
