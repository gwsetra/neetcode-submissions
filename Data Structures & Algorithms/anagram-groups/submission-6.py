class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict()

        for item in strs:
            keymap = [0] * 26
            for char in item:
                # print(ord(char))
                keymap[ord(char)-ord('a')] += 1
            group[tuple(keymap)].append(item)



        return (list(group.values()))