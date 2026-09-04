class MyHashSet:
    # using bit

    def __init__(self):
        self.myset = [False] * 1000001
        # print(self.myset)

    def add(self, key: int) -> None:
        if not self.myset[key]:
            self.myset[key] = True

    def remove(self, key: int) -> None:
        if self.myset[key] is not False:
            tmp = self.myset[key]
            self.myset[key] = False



    def contains(self, key: int) -> bool:

        return self.myset[key] is not False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)