class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for item in strs:
            itemlen = len(item)
            res.append(f'{itemlen}#{item}')
        joined_all = str(''.join(res))
        print(joined_all)
        return joined_all
        
    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        slen = len(s)
        # print('slen', slen)
        if slen == 0:
            return []
        else:
            while pointer < slen:
                print('current pointer', pointer)
                wordcount = int(s[pointer])
                tmp = ''
                for item in range(pointer+2, pointer+wordcount+2, 1):
                    print(item)
                    tmp+=s[item]
                print(tmp)
                res.append(tmp)
                
                pointer += pointer+wordcount+2
        return res