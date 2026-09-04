class StringIterator:

    def __init__(self, compressedString: str):
        # print(compressedString)
        self.ptr = 0
        self.strs = compressedString
        self.strlen = len(compressedString)
        self.curchar = ''
        self.curcharcnt = ''
        self.charcounter = 0

    def getcharcnt(self):
        tmps = self.ptr
        while '0' <= self.strs[tmps+1] <= '9':
            tmps += 1
        return self.strs[self.ptr+1: tmps+1]


    def next(self) -> str:
        if self.ptr >= self.strlen:
            return ''
        
        self.curchar = self.strs[self.ptr]
        self.curcharcnt = self.getcharcnt()

        self.charcounter += 1

        if self.charcounter == int(self.curcharcnt):
            self.ptr = self.ptr + len(self.curcharcnt) + 1
            self.charcounter = 0
        
        return self.curchar

    def hasNext(self) -> bool:
        return self.ptr <= self.strlen-1


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
