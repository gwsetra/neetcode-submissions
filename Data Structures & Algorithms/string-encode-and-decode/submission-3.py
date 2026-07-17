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
        return '|||'.join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == '':
            print('1')
            return []
        if s == '|||':
            print('2')
            return ['']
        # print(s)
        print('3')
        res = s.split('|||')
        return res