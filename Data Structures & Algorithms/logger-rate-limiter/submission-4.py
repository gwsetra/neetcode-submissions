class Logger:

    def __init__(self):
        self.maps = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # print(timestamp, message)
        
        if message not in self.maps:
            self.maps[message] = timestamp
            return True
        
        print(self.maps)
        if timestamp >= self.maps[message]+10:
            self.maps[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
