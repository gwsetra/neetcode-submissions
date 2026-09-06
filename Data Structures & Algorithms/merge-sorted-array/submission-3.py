class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return nums1
        
        num1len = len(nums1)
        num2len = len(nums2)

        for i in range(num2len):
            nums1[m+i] = nums2[i]

        print(nums1)

        
        i = 0
        ptrl = 0
        ptrr = m
        # for i in range(num1len-1):
        while i <= ptrr:
            print(nums1[i], nums1[ptrr], i, ptrr)
            if nums1[ptrr] < nums1[i]:
                tmp = nums1[i]
                nums1[i] = nums1[ptrr]
                nums1[ptrr] = tmp
                ptrr += 1

                if ptrr == num1len:
                    ptrr = m
            else:
                i += 1
            print(nums1, i, ptrr)
        return nums1