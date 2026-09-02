class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        
        for i in range(len(shift)):
            if shift[i][0] == 0:
                net -= shift[i][1]
            else:
                net += shift[i][1]
            # print(net)
        print(net)
        if abs(net) > len(s):
            net = net % len(s)
        print(net)
        if net > 0:
            return s[-net:]+s[:-net]
        elif net < 0:
            net = abs(net)
            print(s[net:], '*', s[:net])
            return s[net:]+s[:net]
        else:
            return s
        
