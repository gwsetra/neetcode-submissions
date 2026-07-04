class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        # print(nums)
        def dfs(is_skip, curidx):
            # print('------**----')
            # print(is_skip, curidx)
            if curidx in cache:
                return cache[curidx]
            if curidx >= len(nums):
                # print('im returning', nums[curidx])
                # if curidx not in cache:
                #     cache[curidx] = nums[curidx]
                return 0

            # print('going into another dfs')

            current_max = max(0 + dfs(True, curidx+1), nums[curidx]+dfs(False, curidx+2))
            # print('after dfs current_max', current_max)
            # print(is_skip, curidx)
            cache[curidx] = current_max
            return  current_max

        if len(nums) == 2:
            return max(nums[0], nums[1])
        return dfs(False, 0)