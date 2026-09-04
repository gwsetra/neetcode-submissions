class StringIterator:

    def __init__(self, compressedString: str):
        self.ptr = 0
        self.strs = ''
        while self.ptr < len(compressedString):
            tmp = self.ptr + 1
            apb = compressedString[self.ptr]
            # print(ptr+1, compressedString[ptr+1], len(compressedString)-1)
            if  self.ptr+1 != len(compressedString)-1 and compressedString[tmp+1].isdecimal():
                tmp += 1
            num = int(compressedString[self.ptr+1 : tmp+1])
            # print(apb, num)

            self.ptr = tmp +1
            # break

            for i in range(num):
                self.strs = self.strs + apb
        # print(self.strs)
        self.ptr = 0

        # print(strs)

    def next(self) -> str:
        if self.ptr >= len(self.strs):
            return ''
        
        tmp = self.strs[self.ptr]
        self.ptr += 1
        return tmp

    def hasNext(self) -> bool:
        return self.ptr <= len(self.strs)-1


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
