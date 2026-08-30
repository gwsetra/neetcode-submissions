class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashset = defaultdict(set)
        hashset = {}
        rp = 0
        res = []

        for i in range(len(nums2)):
            # print(nums2[i])
            hashset[nums2[i]] = i
        
        # print(hashset)
        for i in range(len(nums1)):
            # print(nums1[i], hashset[nums1[i]])
            res.append(hashset[nums1[i]])
        
        return res