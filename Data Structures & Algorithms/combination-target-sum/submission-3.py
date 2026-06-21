class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        hand = []
        finallist = []
        def comb_sum(level, lists):
            # print('*******')
            if sum(hand) == target:
                # print('sum equal to target found')
                finallist.append(hand.copy())
                return 
            if level == len(lists):
                # print('run out of option')
                return 
            elif sum(hand) > target:
                # print('sum exceed target ')
                return 

            # print(level, lists, hand)
            hand.append(lists[level])

            comb_sum(level, lists)

            
            # print("before pop", level, lists, hand)
            hand.pop()
            # print("after pop", level, lists, hand)

            comb_sum(level+1, lists)
        
        comb_sum(0, nums)
        return finallist