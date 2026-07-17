class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for item in strs:
            res.append(f'{len(item)}#{item}')
        # print(joined_all)
        return str(''.join(res))
        
    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        slen = len(s)
        wordcounter = ''
        tmp = ''
        # print('slen', slen)
        if slen == 0:
            return []
        else:
            while pointer < slen:
                # print('current pointer', pointer)
                if s[pointer] != '#':
                    wordcounter += s[pointer]
                    pointer += 1
                else:
                    # print('current tmp value', wordcounter)
                    wordcount = int(wordcounter)
                    if wordcount == 0:
                        res.append('')
                    else:
                        for item in range(pointer+1, pointer+wordcount+1, 1):
                            # print(item)
                            tmp+=s[item]
                        # print(tmp)
                        res.append(tmp)
                    
                    pointer += wordcount+1
                    wordcounter = ''
                    tmp = ''
        return res