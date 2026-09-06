class Solution:
    # starting from biggest
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            m==1
        p1 = m-1
        p2 = n-1
        pc = len(nums1) - 1
        if n == 0:
            return nums1
        
        for i in range(pc, -1, -1):
            # print('***')
            # print(i, nums1[p1], nums2[p2])
            if nums1[p1] < nums2[p2]:
                # print('xx')
                tmp = nums1[i]
                nums1[i] = nums2[p2]
                # nums1[p2] = tmp
                p2 -= 1
            else:
                # print('yyy', )
                tmp = nums1[i]
                nums1[i] = nums1[p1]
                # nums1[p1] = tmp
                p1 -= 1
            
            if p1 == -1 or p2 == -1:
                break
            # print(nums1, nums2)

        # print(nums1, p1, p2, i)

        tmp = nums2 if p1 == -1 else nums1
        # print(tmp)

        # print('finishing')
        for x in range(i-1, -1, -1):
            # print(x)
            nums1[x] = tmp[x]

        # print(nums1) 
            
        


