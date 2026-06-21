class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        if len(s) <= 1:
            return False
        for index, item in enumerate(s):
            print(item)
            print(tmp)
            if item in ('(', '{', '['):
                tmp.append(item)
            else:
                if len(tmp) <= 0:
                    return False
                else:
                    if item == ')' and tmp[-1] == '(':
                        tmp.pop()
                    elif item == '}' and tmp[-1] == '{':
                        tmp.pop()
                    elif item == ']' and tmp[-1] == '[':
                        tmp.pop()
                    else: 
                        return False
                    
        return True