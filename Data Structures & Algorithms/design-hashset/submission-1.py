class MyHashSet:

    def __init__(self):
        self.myset = []

    def add(self, key: int) -> None:
        if key not in self.myset:
            self.myset.append(key)
        # print(self.myset)

    def remove(self, key: int) -> None:
        idx = None
        for i in range(len(self.myset)):
            if key == self.myset[i]:
                idx = i
        if idx:
            self.myset.pop(idx)

    def contains(self, key: int) -> bool:
        return key in self.myset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)