class Solution:

    def encode(self, strs: List[str]) -> str:
        # print(strs)
        # self.decode()
        return '|||'.join(strs)

    def decode(self, s: str) -> List[str]:
        # print(s)
        res = s.split('|||')
        return res