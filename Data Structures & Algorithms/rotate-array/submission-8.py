class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) if k > len(nums) else k
        rp = len(nums)-k
        remainder = rp-k
        lp = 0
        
        print(remainder, rp)

        for i in range(rp, len(nums)):
            print(i)
            tmp = nums[lp]
            nums[lp] = nums[i]
            nums[i] = tmp
            rp += 1
            lp += 1
        
        print(remainder, lp,rp )
        
        tp = lp
        if remainder > 0:
            while tp < len(nums)-1:
                # print(tp)
                tmp = nums[tp]
                nums[tp] = nums[tp+1]
                nums[tp+1] = tmp
                tp += 1
            # print(nums)