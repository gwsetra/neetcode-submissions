class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashset = defaultdict(set)
        hashset = []
        rp = 0

        alls = [x for x in range(len(nums2))]

        for i in range(len(nums1)):
            range2 = set(alls)-set(hashset)
            # print(range2)

            for x,z in enumerate(range2):
                if nums1[i] == nums2[z]:
                    hashset.append(z)

        return hashset