class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)

        maxlength = 0
        loop = 0

        for num in hashmap:
            # print(num)

            if num-1 not in hashmap:
                tmplength = 1
                nextnum = num+1
                while nextnum in hashmap:
                    tmplength += 1
                    nextnum += 1
                maxlength = max(maxlength, tmplength)
        return maxlength