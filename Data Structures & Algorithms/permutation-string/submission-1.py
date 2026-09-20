class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1set = set(s1)
        # print(len(s2), len(s1), len(s2)-len(s1))

        for i in range(len(s2)-len(s1)+1):
            print(s1set, set(s2[i:i+len(s1)]), s1set == set(s2[i:i+len(s1)]))
            if s1set == set(s2[i:i+len(s1)]):
                return True
        return False