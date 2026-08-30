class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashset = defaultdict(set)
        hashset = []
        rp = 0

        for i in range(len(nums1)):
            rp = 0
            while nums1[i] != nums2[rp]:
                rp += 1
            # hashset.add(rp)
            hashset.append(rp)
        # print(hashset)

        return hashset