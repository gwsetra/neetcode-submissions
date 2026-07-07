class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        res = []

        for item in strs:
            sorteditem = sorted(item)
            sorteditem = "".join(sorteditem)
            if sorteditem not in group:
                group[sorteditem] = [item]
            else:
                group[sorteditem].append(item)
            
        # print(group.val())

        for key, val in group.items():
            res.append(val)
        
        return res