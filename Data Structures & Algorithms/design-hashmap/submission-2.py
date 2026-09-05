class MyHashMap:

    def __init__(self):
        self.maps = [False] * 1000001

    def put(self, key: int, value: int) -> None:
        self.maps[key] = value

    def get(self, key: int) -> int:
        if self.maps[key] is not False:
            return self.maps[key]
        
        return -1

    def remove(self, key: int) -> None:
        self.maps[key] = False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)