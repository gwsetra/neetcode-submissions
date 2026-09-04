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
        # print('inside getcharcnt', tmps)
        while '0' <= self.strs[tmps+1] <= '9':
            # print('inside loop')
            tmps += 1
            # print(tmps)
        return self.strs[self.ptr+1: tmps+1]


    def next(self) -> str:
        # print('**')
        if self.ptr >= len(self.strs):
            return ''
        
        self.curchar = self.strs[self.ptr]
        self.curcharcnt = self.getcharcnt()
        print(self.curchar, self.curcharcnt)

        self.charcounter += 1

        if self.charcounter == int(self.curcharcnt):
            print('go to next char')
            self.ptr = self.ptr + len(self.curcharcnt) + 1
            self.charcounter = 0
            # print(self.ptr)
        
        return self.curchar



    def hasNext(self) -> bool:
        return self.ptr <= len(self.strs)-1


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
