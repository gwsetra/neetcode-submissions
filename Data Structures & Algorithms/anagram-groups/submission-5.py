class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict()

        for item in strs:
            keymap = [0] * 26
            for char in item:
                # print(ord(char))
                keymap[ord(char)-ord('a')] += 1
            if tuple(keymap) not in group:
                group[tuple(keymap)] = [item]
            else:
                group[tuple(keymap)].append(item)



        return (list(group.values()))