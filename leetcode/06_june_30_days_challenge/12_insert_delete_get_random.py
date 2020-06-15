import random as r

class RandomizedSet:

    def __init__(self):
        self.array = set()

    def insert(self, val: int) -> bool:
        if val in self.array:
            return False
        self.array.add(val)
        return True


    def remove(self, val: int) -> bool:
        if val in self.array:
            self.array.remove(val)
            return True
        return False


    def getRandom(self) -> int:
        return r.choice(list(self.array))

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1)) #True
print(obj.remove(2)) #False
print(obj.insert(2)) #True
print(obj.getRandom()) #1 or 2
print(obj.remove(1)) #True
print(obj.insert(2)) #False
print(obj.getRandom()) #2
