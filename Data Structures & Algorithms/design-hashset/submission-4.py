class MyHashSet:

    def __init__(self):
        self.myset = [None] * 1000000
        # print(self.myset)

    def add(self, key: int) -> None:
        if self.myset[key] is None:
            self.myset[key] = key

    def remove(self, key: int) -> None:
        if self.myset[key]:
            tmp = self.myset[key]
            self.myset[key] = None



    def contains(self, key: int) -> bool:
        return self.myset[key] is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)