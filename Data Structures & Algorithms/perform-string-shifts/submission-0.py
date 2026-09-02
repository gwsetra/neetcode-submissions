class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        
        for i in range(len(shift)):
            if shift[i][0] == 0:
                net -= shift[i][0]
            else:
                net += shift[i][0]

        if net > 0:
            return s[-net:]+s[:-net]
        elif net < 0:
            return s[net:]+s[:net]
        else:
            return s
        
