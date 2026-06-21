class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for index, item in enumerate(s):
            print(item)
            print(tmp)
            if item in ('(', '{', '['):
                tmp.append(item)
            elif item == ')' and tmp[-1] == '(':
                tmp.pop()
            elif item == '}' and tmp[-1] == '{':
                tmp.pop()
            elif item == ']' and tmp[-1] == '[':
                tmp.pop()
            else: 
                return False
        return True