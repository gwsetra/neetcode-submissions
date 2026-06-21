class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {} # value, index
        index = 0

        for loop, item in enumerate(nums):
            tmpresult = target-item
            print('tmpresult', tmpresult)

            if tmpresult not in mymap:
                mymap[item] = index
                print("mymap:", mymap)
                index += 1
            else:
                print('MATCH FOUND')
                return [mymap[tmpresult], loop]