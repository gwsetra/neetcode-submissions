class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            # print('a')
            return str()
        if strs == ['']:
            # print('b')
            return '|||'
        # print(strs)
        # self.decode()
        # print('c')
        encode = ''
        for item in strs:
            # print(item)
            if item == '':
                encode += str({0:''}) + '|||'
            else:
                # encode += str(len(item)) + item + '|||'
                encode += str({str(len(item)):item}) + '|||'
        # return '|||'.join(strs)
        # print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        # print(s)
        if s == '':
            # print('1')
            return []
        if s == '|||':
            # print('2')
            return ['']
        
        splitted = s.split('|||')
        res = []
        # print(splitted)
        for item in splitted:
            if item == '':
                continue
            if item[0] == 0:
                res.append('')
            else:
                # print(item)
                for counts,word in eval(item).items():
                    # print(x, y)
                    res.append(word)
                # print(next(iter(eval(item
                
        # print(res)
        return res