class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        return math.ceil(sum(people)/limit)