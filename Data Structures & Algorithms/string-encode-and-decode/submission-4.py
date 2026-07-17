class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            print('a')
            return str()
        if strs == ['']:
            print('b')
            return '|||'
        # print(strs)
        # self.decode()
        print('c')
        encode = ''
        for item in strs:
            print(item)
            if item == '':
                encode += '0'+ '|||'
            else:
                encode += str(len(item)) + item + '|||'
        # return '|||'.join(strs)
        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == '':
            print('1')
            return []
        if s == '|||':
            print('2')
            return ['']
        
        splitted = s.split('|||')
        res = []
        print(splitted)
        for item in splitted:
            if item == '':
                continue
            if item[0] == 0:
                res.append('')
            else:
                res.append(item[1:])
        print(res)
        return res