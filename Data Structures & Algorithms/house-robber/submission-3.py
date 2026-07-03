class Solution:
    def rob(self, nums: List[int]) -> int:
        # print(nums)
        def dfs(is_skip, curidx):
            # print('------**----')
            # print(is_skip, curidx)
            if curidx+1 > len(nums)-1 or curidx+2 > len(nums)-1:
                # print('im returning', nums[curidx])
                return nums[curidx]

            # print('going into another dfs')

            current_max = max(0 + dfs(True, curidx+1), nums[curidx]+dfs(False, curidx+2))
            # print('after dfs current_max', current_max)
            # print(is_skip, curidx)
            return  current_max
        return dfs(False, 0)