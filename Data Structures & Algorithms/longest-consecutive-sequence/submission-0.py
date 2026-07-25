class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)

        maxlength = 0
        loop = 0

        for num in hashmap:
            # print(num)

            if num-1 not in hashmap:
                tmplength = 1
                tmp = num
                while True and loop < 10:
                    
                    if tmp+1 not in hashmap:
                        break
                    
                    tmplength += 1
                    tmp += 1
                    loop += 1
                maxlength = max(maxlength, tmplength)
        return maxlength