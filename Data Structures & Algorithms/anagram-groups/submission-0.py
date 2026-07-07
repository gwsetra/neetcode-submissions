class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        res = []

        for item in strs:
            asciirep = 0
            # print(item)
            for char in item:
                # print(char)
                asciirep += ord(char)
            if asciirep not in sets:
                sets[asciirep] = [item]
            else:
                sets[asciirep].append(item)
            
        # print(sets)

        for key, val in sets.items():
            res.append(val)
            # print(key, val)
        
        return res