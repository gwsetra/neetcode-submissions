class Solution:
    # merge sort
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.mergesort(0, len(nums)-1)

        return self.nums
    
    def mergesort(self, si, ei):
        mid = ((ei-si) // 2) + si
        # print(self.nums[si:ei+1], si, mid, ei)

        if ei-si < 1:
            # print('return')
            # print(self.nums[si])
            return (self.nums[si:ei+1] or [])

        # print('going for first mergesort')
        arr1 = self.mergesort(si, mid)
        arr2 = self.mergesort(mid+1, ei)
        # print('arr1+arr2',arr1, arr2)

        return self.merge(si, mid, ei, arr1, arr2)

    def merge(self, si, mid, ei, arr1, arr2):
        # print('inside merge', si, mid, ei, self.nums, arr1, arr2)
        x = si
        l = 0
        r = 0

        while l < len(arr1) and r < len(arr2):
            # print('lets compare: ',arr1[l], arr2[r])
            if arr1[l] < arr2[r]:
                # print(f"{arr1[l]} is smaller than {arr2[r]}")
                self.nums[x] = arr1[l]
                l += 1
            else:
                # print(f"else",)
                self.nums[x] = arr2[r]
                r += 1
            x+=1
        
        while l < len(arr1):
            # print('lets compare left only', arr1[l:])
            self.nums[x] = arr1[l]
            l += 1
            x += 1
        
        while r < len(arr2):
            # print('lets compare left only', arr2[r:])
            self.nums[x] = arr2[r]
            r += 1
            x += 1

        # print('final merge:', self.nums[si:ei+1])

        return self.nums[si:ei+1]
